user=int(input("enter num="))#how many numbers you want
index=1
a=[ ]#emptylist for appending odd numbers
count=0
while index<50:
    if index%2!=0:#for odd num
        count+=1
        a.append(index)
        if count==user:
            break#for exit fron loop
    index+=1
print(a)