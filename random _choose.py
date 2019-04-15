#encoding:utf-8
import random
from random import randint
'''
ROBBERY
BATTERY
SEX OFFENSE
THEFT
KIDNAPPING
HUMAN TRAFFICKING
'''


filepath='2015_HUMAN TRAFFICKING.csv'

count = 0
for index, line in enumerate(open(filepath,'r')):
    count += 1
print(count)


oldf=open(filepath,'r')
newf=open('random_'+filepath,'w')
n = 0
if count<1000:
    resultList= random.sample(range(1,count),count-1)
else:
    resultList = random.sample(range(1,count),1000) # sample(x,y)函数的作用是从序列x中，随机选择y个不重复的元素。
 
lines=oldf.readlines()

newf.write(lines[0])
for i in resultList:
    newf.write(lines[i])
oldf.close()
newf.close()
