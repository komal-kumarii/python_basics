num=[50,40,23,70,56,12,5,10,7]
index=0
b=num[index]
while index<len(num):
    if b>num[index]:
        b=num[index]
    index+=1
print("min",b)