import json
s1 = '"Abcadf"'
s2 = '["123", "4556", 1234, "abcad", "Abcadf"]'
s3 = '{"Abcadf": "123", "is_available": false}'
i1 = '5555'
i2 = '3.14'
t = 'true'
f = 'false'
n = 'none'

json_s1 = json.loads(s1)
print(json_s1)
json_s2 = json.loads(s2)
print(json_s2)
json_s3 = json.loads(s3)
print(json_s3)
json_i1 = json.loads(i1)
print(json_i1)
json_i2 = json.dumps(i2)
print(json_i2)
json_t = json.dumps(t)
print(json_t)
json_f = json.dumps(f)
print(json_f)
json_n = json.dumps(n)
print(json_n)

