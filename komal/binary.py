binary_num=[1,0,0,1,1,0,1,1]
index=len(binary_num)-1
count=0
sum=0
while index>=0#reverse loop
    a=binary_num[index]*2**count#for exponent
    sum+=a#sum of num
    count+=1
    index-=1#decrement
print(sum)#convert into decimal