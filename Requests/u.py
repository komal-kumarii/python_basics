import json
# empl_list=["emp1","emp2","emp3","emp4"]
key=["name","designation","age","salary"]
empl=[["neelam","programer","24","2400"],
["komal","trainer","24","20000"],
["anuradha","HR","25","40000"],
["Ahisheck","manager","29","63000"]]
employee={}
for i in empl:
	empl1={}
	lis=[]
	for j in i:
		lis.append(j)
		data=dict(zip(key,lis))
	empl1.update(data)
	employee.update(empl1)
	print(employee)
	a={}
	a.update(employee)
my_file=open("nested.json","w")
data=json.dump(a,my_file,indent=4)
print(data)