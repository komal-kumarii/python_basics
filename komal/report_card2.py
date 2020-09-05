marks=[
    [78,76,94,86,88],
    [91,71,98,65],
    [95,45,78],
    [87,67,49,68,88],
]
index=0
count=0
while index<len(marks):
    j=0
    sum=0#for sum of row elements
    while j<len(marks[index]):
        sum+=marks[index][j]
        count+=1
        if count==len(marks[index]):
            break #for next row
        j+=1
    average=sum//len(marks[index])#for average
    print("average",average)
    index+=1
    
