elements=[23,14,56,12,19,9,15,25,31,42,43]
even=0
odd=0
count=0
sum=0
sum_even=0
sum_odd=0
index=0
while index<len(elements):
    if elements[index]%2==0:#even num
        even+=1
        count+=1#count even num
        sum+=elements[index]#sum of element
        sum_even+=elements[index]#sum of even num
    else:
        odd+=1#odd num
        count+=1#count odd num
        sum+=elements[index]#sum of element
        sum_odd+=elements[index]#sum of odd num
    index+=1
average_even=sum_even/even
average_odd=sum_odd/odd
print("average_even",average_even)
print("average_odd=,"average_odd)
print("even num=",even)
print("odd num",odd)
print("total num=",count)
print("total sum=",sum)
print("sum_even",sum_even)
print("sum_odd=",sum_odd)