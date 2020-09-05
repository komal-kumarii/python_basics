num=[50,40,23,70,56,12,5,10,7]
max1=0
max2=0
index=0
while index<len(num):
    if num[index]>max1:
        max1=num[index]#maximum
    index+=1
    j=0
    while j<len(num):
        if max1>num[j] and max2<num[j]:#for second max
            max2=num[j]#swapping
        j+=1
print(max2)