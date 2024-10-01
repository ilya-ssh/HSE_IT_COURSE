import json
print('Before: ')
with open('sample.json') as file:
    data = json.load(file)
    pretty_json = json.dumps(data, indent=4)
    print(pretty_json)
for d in data['BorrowedBy']:
    del d['BorrowedDate']
with open('sample_edited.json', 'w') as file:
    json.dump(data, file, indent=4)
print('After: ')
with open('sample_edited.json', 'r') as file:
    data = json.load(file)
    pretty_json = json.dumps(data, indent=4)
    print(pretty_json)
