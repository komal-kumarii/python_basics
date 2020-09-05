num=[1,2,3,4,5,6,7,8,9,10]
index=0
even=[ ]
odd=[ ]
while index<len(num):
    if num[index]%2==0:
        even.append(num[index])
    else:
        odd.append(num[index])
    index+=1
print(even)
print(odd)