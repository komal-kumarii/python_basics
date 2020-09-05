dic1={1:10, 2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
d={}
for i,j in dic1.items():
	for x,y in dic2.items():
		if i==x:
			c={i:j+y}
			d.update(c)
		else:
			if i not in d:
				d.update(dic1)
				d.update(dic2)
				d.update(dic3)
print(d)