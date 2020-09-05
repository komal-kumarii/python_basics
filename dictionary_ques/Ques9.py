word="MISSISSIPPI"
d={}
for i in range(0,len(word)):
	j=i+1
	count=0
	for j in range(0,len(word)):
		if word[i]==word[j]:
			count+=1
			d[word[i]]=count
print(d)
