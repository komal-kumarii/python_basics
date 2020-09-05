lis=["-2","0","-9","45","11"]
empty_lis=[ ]
index=0
while index<len(lis):#for iterating elements
    j=index#for next element
    while j<len(lis):
        if lis[index]>lis[j]:
            lis[index],lis[j]=lis[j],lis[index]#swapping 
        j+=1
    empty_lis.append(lis[index])
    index+=1
print(empty_lis)