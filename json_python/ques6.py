import json
json_string={ "a":  1,
"a":  2,
"a":  5, 
"a": 4, 
"b": 1,
"b":2}
# print(json_string)
data=json.dumps(json_string)
print(data)