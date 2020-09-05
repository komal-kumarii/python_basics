a=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
crore=0
lakh=0
dilwale=0
i=0
while i<len(a):
    if a[i]>=10000000:
        crore+=1
    elif a[i]>=100000 and a[i]<10000000:
        lakh+=1
    else:
        dilwale+=1
    i+=1
print("crorrepati=",crore)
print("lakhpati",lakh)
print("dilwaale",dilwale)