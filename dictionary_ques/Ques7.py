dic=[
     {"first":"1"}, 
     {"second": "2"}, 
     {"third": "1"}, 
     {"four": "5"}, 
     {"five":"5"}, 
     {"six":"9"},
     {"seven":"7"}
]
d=[]
for i in range(0,len(dic)):
	for j in dic[i]:
		if dic[i][j] not in d:
			d.append(dic[i][j])
print(d)