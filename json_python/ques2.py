import json
my_file=open("user2.json","w")
my_data={"name": "David",
     "class":"I",
     "age": 6 }
data= json.dump(my_data,my_file,indent=4)
print(data) 
#you have to see result in user2.json