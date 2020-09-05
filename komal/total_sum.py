n=[10,11,12,13,14,17,18,19]
num=30
a=[]#big_list
index=0
while index<len(n):
    j=index+1#for next element
    b=[]#empty list
    while j<len(n):
        if n[index]+n[j]==num:#compare
            b.append(n[index])#sublist
            b.append(n[j])#sublist
            a.append(b)#big_list
        j+=1
    index+=1
print(a)