import pandas as pd

file_name="Chicago_Crimes_all_2014.csv"
fr=pd.read_csv(file_name)
data=pd.DataFrame(fr)

data_Date=data['Date']
month=[]
day=[]
for item in data_Date:
    #print(item)
    month.append(item[0:2])
    day.append(item[3:5])

data['month']=month
data['day']=day

data.to_csv("new_"+file_name)
    
    
