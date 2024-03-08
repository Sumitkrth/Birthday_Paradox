import random
from date import random_dates

#print(random_dates)

i=0
flag=0
count=0
repetition=[]

while(i<len(random_dates)-1):
    if(random_dates[i]==random_dates[i+1]):
        count=count+1
        rep=((f"{random_dates[i]}, {random_dates[i+1]} at the position {i},{i+1}"))
        repetition.append(rep+'\n')
        flag=1
    i=i+1
if count==1:
    print(f" {count} repetition is present:")
if count>1:
    print(f" {count} repetition are present:")
print("".join(repetition))
if (flag == 0):
    print("There is no repetition")
