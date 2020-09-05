my_dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
new_dict={}
for i,j in my_dic.items():
	for x,y in my_dic.items():
		if j>y:
			i=x
			a={i:y}
			new_dict.update(a)
if my_dic[x] not in new_dict:
	new_dict.update(my_dic)
print(new_dict)