marks=[
    [78,76,94,86,88],
    [91,71,98,65,76],
    [95,45,78,52,49],
]
index=0
sum=0#for sum
while index<len(marks):#for iterate
    j=0
    while j<len(marks[index]):#for accesing row elements 
        sum+=marks[index][j]
        j+=1
    index+=1
print(sum)