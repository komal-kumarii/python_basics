char=["a","n","t","a","a","t","n","n","a","x","u","g","a","x","a"]
empty_lis=[]
index=0
while index<len(char):
    if char[index] not in d:#appending single element in empty_lis
        empty_lis.append(char[index])
    index+=1
print(empty_lis)#list of single elements
j=0
empty_list2=[]
while j<len(empty_lis):
    k=0
    count=0
    c=[]#emptylist
    while k<len(char):
        if empty_lis[j]==char[k]:#compare and count
            count+=1
        k+=1
    c.append(empty_lis[j])
    c.append(count)
    empty_list2.append(c)
    print(empty_lis[j],count,"times")
    j+=1
print(empty_list2)