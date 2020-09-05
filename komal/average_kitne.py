elements=[23,14,56,12,19,9,15,25,31,42,43]
even=0
odd=0
sum_even=0
sum_odd=0
i=0
while i<len(elements):
    if elements[i]%2==0:
        sum_even+=elements[i]
        even+=1
    else:
        sum_odd+=elements[i]
        odd+=1
    i+=1
average_even=sum_even/even
average_odd=sum_odd/odd
print(average_even)
print(average_odd)