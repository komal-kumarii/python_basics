import json
string={'4': 5, 
 '6': 7, 
 '1': 3, 
 '2': 4}
data=json.dumps(string,sort_keys=True,indent=2)
print(data)