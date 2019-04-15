#coding:utf-8
import pandas as pd
import numpy as np

for ye in range(2015,2016):
    file_name="new_Chicago_Crimes_all_"+str(ye)+".csv"
    fr=pd.read_csv(file_name)
    data=pd.DataFrame(fr)

    data=data.dropna(subset=['Longitude'])
    '''
    for i in range(len(data)):
      if np.isnan(data['Longitude'][i]):
        data = data.drop(i)
    '''
    
    data.to_csv("drop_"+file_name)
    print(ye)
