import json
json_string='{"Name":"Ram", "Class":"IV", "Age":9 }'
my_data=json.loads(json_string)
print(my_data)