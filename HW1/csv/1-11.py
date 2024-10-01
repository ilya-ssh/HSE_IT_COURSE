import csv
import random
import string
files = {
    'custom3.csv':',',
    }
names = []
di_data= {}
for _ in range(5):
    name_length = random.randint(1, 10)
    random_name = ''.join(random.choices(string.ascii_uppercase, k=name_length))
    names.append(random_name)
for name in names:
    random_values = []  
    for _ in range(3):
        random_value = random.randint(1, 1000)
        random_values.append(random_value)  
    di_data[name] = random_values
print(di_data)  
for file, delimeter in files.items():
    with open(file, 'wt',  newline='') as table:
        write = csv.DictWriter(table, names)
        write.writeheader()
        rows = zip(*di_data.values())
        for row in rows:
            write.writerow(dict(zip(names, row)))
for file, delimeter in files.items():
    with open(file, 'r') as table:
        text = csv.reader(table, delimiter=delimeter, skipinitialspace=True)
        for x in text:
            print(','.join(x))
