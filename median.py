import csv 
with open('data.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
new_data=[]
for  i in range(len(file_data)):
    n= file_data[i][2] 
    new_data.append(float(n))
    
nl=len(new_data)
new_data.sort()
if nl%2 ==0:
    m1=float(new_data[nl//2])
    m2=float(new_data[nl//2-1])
    m=(m1+m2)/2
else:
    m=new_data[nl//2]
print("median is "+str(m))
