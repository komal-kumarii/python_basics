# import json
# my_file=open("Ques1.json","w")
# my_dict={"place":"taj","locat":"agra"}
# my_data=json.dumps(my_dict)
# print(my_data)
# print(type(my_data))
import json
data = {'people':[{'name': 'Scott', 'website': 'stackabuse.com', 'from': 'Nebraska'}]}
a=json.dumps(data,sort_keys=True,indent=4,ensure_ascii=False)
print(a)