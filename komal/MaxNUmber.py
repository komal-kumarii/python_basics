num=[50,40,23,70,56,12,5,10,7]
index=0
a=num[0]
while index<len(num):
    if a<num[index]:
        a=num[index]
    index+=1
print("max",a)