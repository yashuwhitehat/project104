import csv 
from collections import Counter
from mimetypes import init
from statistics import mode
with open('data.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
new_data=[]
for  i in range(len(file_data)):
    n= file_data[i][2] 
    new_data.append(float(n))
    
data=Counter(new_data)
mode_data={"50-60":0,"60-70":0,"70-80":0}
for h,o in data.items():
    if 50<float(h)<60:
        mode_data["50-60"]+=o
    elif 60<float(h)<70:
        mode_data["60-70"]+=o
    elif 70<float(h)<80:
        mode_data["70-80"]+=o
mode_r,mode_o=0,0
for r,o in mode_data.items():
    if o>mode_o:
       mode_r,mode_o=[int(r.split("-")[0]),int(r.split("-")[1])],o
mode =float((mode_r[0] + mode_r[1]) /2)
print(f"Mode is -> {mode:2f}")