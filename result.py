import pandas as pd
import numpy as np 
import os
import csv


s=os.listdir()

list_res=[]

with open("result_show.csv","w",newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["name","best","top10%","top20%"])
    for file in s:
        if ("_Result_" in file):
            csv_frame=pd.read_csv(file)
            data=pd.DataFrame(csv_frame)
            KDE=data['KDE']
            a = np.array(KDE)
            b = np.argsort(a)
            print(file+" ",a[b[-1]],"  ",a[b[-756]],"  ",a[b[-1512]])
            writer.writerow([file,a[b[-1]],a[b[-756]],a[b[-1512]]])


#dataframe = pd.DataFrame({list_res.keys(),list_res.values()})


    
