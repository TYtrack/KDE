#filter_data

import pandas as pd
import numpy as np

year="2015"
file_name="wendu_drop_new_Chicago_Crimes_all_"+year+".csv"
fr=pd.read_csv(file_name)
data=pd.DataFrame(fr)

# SEX OFFENSE
# BATTERY
# ROBBERY
# THEFT
# HUMAN TRAFFICKING
# KIDNAPPING
type_1='KIDNAPPING'
data=data.ix[data['Primary Type']==type_1]


data.to_csv(year+"_"+type_1+".csv")
