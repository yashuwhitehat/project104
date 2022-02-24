import csv 
with open('data.csv',newline='')as f:
    reader=csv.reader(f)
    file_data=list(reader)
file_data.pop(0)
new_data=[]
for  i in range(len(file_data)):
    n= file_data[i][2] 
    new_data.append(float(n))
print(new_data)
nl=len(new_data)
total=0
for  x in new_data:
    total=total+x 
mean=total/nl
print("mean is "+str(mean))
