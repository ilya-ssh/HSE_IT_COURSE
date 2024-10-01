import json
data = '{"a": 1,"a": 2,"c": 2,"d": 3,"c": 1,"d": 4}'
print(f'Unedited data: \n {data}')
json_obj = json.loads(data)
print("Unique keys:")
print(json_obj) 
