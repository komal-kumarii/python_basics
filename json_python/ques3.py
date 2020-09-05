import json
my_dict='{"name":"komal","class":12,"roll no":23}'
my_file=open("nor.json","w")
json_string=json.dump(my_dict,my_file)
print(json_string)
print(type(json_string))