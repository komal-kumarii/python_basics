lis=["n","i","t","i","n"]
index=len(lis)-1
emptylist=[ ]
while index>=0:#for reverse loop
    emptylist.append(lis[index])
    index-=1
print(emptylist)
if emptylist==lis:#for comparison
    print("palinderome")
else:
    print("not palinderome")