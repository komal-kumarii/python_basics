list1=[1,2,3,4,5,6]
list2=[2,3,1,0,6,7]
emptylist=[]
index=0
while index<len(list1):#for iterate list1
    if list1[index] not in list2:#for check elements
        emptylist.append(list1[index]) #appending elements which are not present
    index+=1
print(emptylist)#not present elements