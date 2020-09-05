elements=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
b=[]#emptylist
index=0
while index<len(elements):
    j=index+1#for next element
    while j<len(elements):
        if elements[index]==elements[j]:#its true then append
            b.append(elements[index])
            break#for exit from loop
        j+=1
    index+=1
print(b)