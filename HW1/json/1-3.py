import json
s1 = "Abcadf"
s2 = ['123','4556', 1234, 'abcad', s1]
s3 = {s1: "123", "is_available": False}
i1 = 5555
i2 = 3.14
t = True
f = False
n = None

json_s1 = json.dumps(s1)
print(json_s1)
json_s2 = json.dumps(s2)
print(json_s2)
json_s3 = json.dumps(s3)
print(json_s3)
json_i1 = json.dumps(i1)
print(json_i1)
json_i2 = json.dumps(i2)
print(json_i2)
json_t = json.dumps(t)
print(json_t)
json_f = json.dumps(f)
print(json_f)
json_n = json.dumps(n)
print(json_n)
