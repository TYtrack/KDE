#coding:utf-8
import pickle

import pandas as pd


year="2016"
with open(r"C:\Users\DELL\Desktop\KDE\温度\\"+year+"_weather_dict.pkl",'rb') as f:
    weather_dict = pickle.load(f,encoding='bytes')

data_dict=dict()

for key_name in weather_dict.keys():
    s=weather_dict[key_name][1].decode(encoding="utf-8")
    l=s.split('/')
    if (l==['']):
        continue
    if (l[0]==''):
        aver=int(l[1])
    elif (l[1]==''):
        aver=int(l[0])
    else:
        aver=(int(l[0])+int(l[1]))/2
    data_dict[key_name.decode(encoding="utf-8")]=aver


#has_key

wen_du=[]

file_name="drop_new_Chicago_Crimes_all_"+year+".csv"
fr=pd.read_csv(file_name)
data=pd.DataFrame(fr)
for item in range(len(data)):
    ske=str(data['month'][item])
    hkt=str(data['day'][item])
    if len(ske)==1:
          ske="0"+ske
    if len(hkt)==1:
          hkt="0"+hkt
    if (ske+"/"+hkt) in data_dict.keys()    :
          wen_du.append(data_dict[ske+"/"+hkt])
    else:
          data = data.drop(item)
    if (item%100==0):
        print(item)
data['wendu']=wen_du
data.to_csv("wendu_"+file_name)
          
          

