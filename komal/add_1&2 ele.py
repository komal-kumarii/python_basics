a=[14,5,6,2,9,8,4]
b=[ ]#empty list
index=0
while index<len(a)-1:
    c=a[index]+a[index+1]#for adding 1 and 2 element
    b.append(c)
    index+=2
if len(a)%2!=0:#for even or odd length of num
    d=a[-1]#if odd then print last element
    b.append(d)
print(b)