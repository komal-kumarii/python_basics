places=["delhi","gujarat","rajasthan","punjabi"]
index=len(places)-1
emptylist=[ ]
while index>=0:#for reverse loop
    emptylist.append(places[index])
    index-=1
print(emptylist)#reverse list