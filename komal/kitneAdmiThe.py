elements=[23,14,56,12,19,9,15,25,31,42,43]
index=0
even=0#for count even numbers
odd=0# for count odd numbers
while index <len(elements):#iteratind numbers
    if elements[index]%2==0:#for even num
        even+=1
    else:#for odd num
        odd+=1
    index+=1
print("even num=",even)
print("odd num",odd)