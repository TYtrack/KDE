from scipy.stats import norm
import numpy as np 
import math
import pandas as pd

csv_frame=pd.read_csv("add_hour_random_2015_BATTERY.csv")
data=pd.DataFrame(csv_frame)

#X Coordinate
long=data['Longitude']
lati=data['Latitude']
hour=data['hour']
wendu=data['wendu']


def cha(a,b):
        s=abs(a-b)
    if (s>12):
        return 24-s

    return s

def std_time(list_t):
    means=sum(list_t)/len(list_t)
    sum_1=0
    for i in list_t:
        sum_1+=(cha(i,means)*cha(i,means))
    return sum_1/len(list_t)

'''

place=[] 

for item in range(len(long)):
    s1=math.floor((87.9264825125+long[item])/0.0015069549/3)*252/3+math.floor((42.0230678864-lati[item])/0.0015069549/3)
    place.append(s1)

data["dipan"]=place
data.to_csv('DATAAA'+'.csv')

'''


'''
for item_long in np.arange(-87.9264825125,-87.5241255435,0.0015069549):
        for item_lati in np.arange(42.0230678864,41.6448221965,-0.0015069549):
            count+=1
            if count%10==0:
                print(count)
            temp_K=0
            for j in range(len(arr_A)):
                temp_K+=(Kernel((item_long-arr_A[j])/bw1)*Kernel((item_lati-arr_B[j])/bw1)*VMD((now_t-arr_H[j])/bw2,k2))
            sum_K=temp_K/(len(arr_A)*bw1*bw1*bw2)
            Long_list.append(item_long)
            Lati_list.append(item_lati)
            KDE.append(sum_K)

'''

def k_sure(list_a):
    r=sum(list_a)/len(list_a)
    k=r-pow(r,3)
    k=k/(1-pow(r,2))
    return k
    

    


#点的个数
p_size=len(long)
print("案件数量："+str(p_size))
#标准差
long_std = np.std(long,ddof=1)
lati_std = np.std(lati,ddof=1)
hour_std = np.std(hour,ddof=1)
wendu_std= np.std(wendu,ddof=1)


#合并标准差 pooled
Sp=math.sqrt(((p_size-1)*pow(long_std,2)+(p_size-1)*pow(lati_std,2))/(2*p_size-2))

print(Sp)
print("Hour STD:"+str(hour_std))
print("wendu STD:"+str(wendu_std))
#核函数1的最佳带宽
h_opti_1=Sp*pow(p_size,-1/6)

#核函数2的最佳参数K
k_opti=1/(pow(hour_std,2))

h_opti_2=hour_std*pow(p_size,-1/6)

h_opti_3=wendu_std*pow(p_size,-1/6)



# -87.9264825125  -87.5241255435
#  42.0230678864   41.6448221965
#   0.0015069549    0.0015069549

#  268*252
#  134*166


'''
def KDE(arr_A,arr_B,now_t,arr_H,bw1,bw2,k2):
    KDE=[]
    Long_list=[]
    Lati_list=[]
    count=0
    for item_long in np.arange(-87.9264825125,-87.5241255435,0.0015069549*3):
        for item_lati in np.arange(42.0230678864,41.6448221965,-0.0015069549*3):
            count+=1
            if count%10==0:
                print(count)
            temp_K=0
            for j in range(len(arr_A)):
                temp_K+=(Kernel((item_long-arr_A[j])/bw1)*Kernel((item_lati-arr_B[j])/bw1)*VMD((now_t-arr_H[j])/bw2,k2))
            sum_K=temp_K/(len(arr_A)*bw1*bw1*bw2)
            Long_list.append(item_long)
            Lati_list.append(item_lati)
            KDE.append(sum_K)
    data = {
    'Longitude':Long_list,
    'Latitude':Lati_list,
    'KDE':KDE
    }
    return data

'''
def KDE_2(arr_A,arr_B,now_t,arr_H,bw1,bw2,k2,arr_W,now_w,bw3):
    KDE=[]
    Long_list=[]
    Lati_list=[]
    count=0
    for item_long in np.arange(-87.9264825125,-87.5241255435,0.0015069549*3):
        for item_lati in np.arange(42.0230678864,41.6448221965,-0.0015069549*3):
            count+=1
            if count%100==0:
                print(count)
            temp_K=0
            for j in range(len(arr_A)):
                temp_K+=(Kernel((item_long-arr_A[j])/bw1)*Kernel((item_lati-arr_B[j])/bw1)*VMD((now_t-arr_H[j])/bw2,k2)*Kernel((now_w-arr_W[j])/bw3))
            sum_K=temp_K/(len(arr_A)*bw1*bw1*bw2*bw3)
            Long_list.append(item_long)
            Lati_list.append(item_lati)
            KDE.append(sum_K)
    data = {
    'Longitude':Long_list,
    'Latitude':Lati_list,
    'KDE':KDE
    }
    return data
     


# 核函数K1
def Kernel(x):
    #normal function 标准正态分布
    y=norm.pdf(x)
    return y

# MBF Modified Bessel Function of the First Kind
def MBF(z):
    sum_M=0
    for k in range(13):
        sum_M+=pow((0.25*z*z),k)/pow(math.factorial(k),2)
    return sum_M


# von Mises distribution 冯米塞斯分布
# 参数t是输入，k就是k
def VMD(t,k):
    k=1
    para=0.12571
    #para=1/(2*math.pi*MBF(k))
    vmd_value=para*math.exp(k*math.cos(t*math.pi/12))
    return vmd_value


t_list=[0,6,12,18,18,18,18,18   ]
w_list=[20,20,20,20,25,10,0,-10 ]
for item_l in range(9):  
    now_t=t_list[item_l]
    now_w=w_list[item_l]
    print(str(now_t)+"<--时间  温度-->"+str(now_w))
    #final=KDE(long,lati,now_t,hour,h_opti_1,h_opti_2,k_opti)
    final=KDE_2(long,lati,now_t,hour,h_opti_1,h_opti_2,k_opti,wendu,now_w,h_opti_3)
    frame = pd.DataFrame(final)
    frame.to_csv('_Result_'+str(now_t)+"_"+str(now_w)+"_SEX OFFENSE.csv")



