index=1
a=[]
while index<=10:
    x=int(input("enter the num"))
    a.append(x)
    index+=1
print(a)
j=0
while j<len(a):
    b=a[j]-a[j+1]
    c=a[j+1]-a[j+2]
    if b!=c:
        print("not progression")
        break
    j+=1
print("progression")
