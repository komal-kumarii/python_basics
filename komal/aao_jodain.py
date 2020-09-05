elements=[23,14,56,12,19,9,15,25,31,42,43]
sum_even=0
sum_odd=0
index=0
while index<len(elements):#iterating elements oflist
    if elements[index]%2==0:#for even num
        sum_even+=elements[index]#for even sum
    else:
        sum_odd+=elements[index]#for odd sum
    index+=1
print(sum_even)
print(sum_odd)