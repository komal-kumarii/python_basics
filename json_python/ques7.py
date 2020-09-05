import json
data=open("text.txt") 
dic={}
for line in data:
	i,j=line.strip().split(None,1)
	dic[i]=j.strip()
my_file=open("user.json","w")
my_data=json.dump(dic,my_file,indent=4)
print(my_data)
#you can see result in user.json file