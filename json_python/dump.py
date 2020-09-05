import json
myfile=open('Ques1.json', 'w')
print(type(myfile))
# my_data = json.load(myfile)
mt_dict={"names":"sia","roll":23}
my_data=json.dump(mt_dict,myfile)
print(type(myfile)) 
print(my_data)