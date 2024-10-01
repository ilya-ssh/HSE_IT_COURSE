import csv
files = {
    'countries.csv':' ',
    'departments.csv':',',
    'employees.csv':',',
    }
for file, delimeter in files.items():
    with open(file, 'r') as table:
        text = csv.reader(table, delimiter=delimeter)
        for x in text:
            print(' '.join(x))
