import csv
files = {
    'countries.csv':' ',
    'departments.csv':',',
    'employees.csv':',',
    }
for file, delimeter in files.items():
    with open(file, 'r') as table:
        text = csv.DictReader(table, delimiter=delimeter)
        rows = list(text)
        for column_name in text.fieldnames:
            print(f"Column: {column_name}")
            for row in rows:
                print(row[column_name])
