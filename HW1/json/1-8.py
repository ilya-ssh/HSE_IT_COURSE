import json
complex_json = '{"__complex__": true, "real": 10, "img": 9}'
simple_json = '{"real": 4, "img": 3}'
complex_object = json.loads(complex_json)
if '__complex__' in complex_object:
    complex_object = complex(complex_object['real'], complex_object['img'])

simple_object = json.loads(simple_json)


print("Complex:", complex_object)
print("Simple:", simple_object)
