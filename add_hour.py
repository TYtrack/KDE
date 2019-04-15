import pandas as pd
import numpy as np

import os
sname = os.listdir()

for akb in sname:
    if ("random_" in akb):
        file_name=akb
        fr=pd.read_csv(file_name)
        data=pd.DataFrame(fr)

        date=data['Date']
        hour=[]

        for i in date:
            ho=int(i[11:13])
            if i[20:22]=='AM':
                hour.append(ho)
            else:
                hour.append((ho+12)%24)

        data['hour']=hour
        data.to_csv("add_hour_"+file_name)
    
