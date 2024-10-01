import csv
files = {
    'countries.csv':' ',
    'departments.csv':',',
    'employees.csv':',',
    }
for file, delimeter in files.items():
    with open(file, 'r') as table:
        text = csv.reader(table, delimiter=delimeter)
        noheader = next(text)
        for x in text:
            print(','.join(x))
        rowcount = text.line_num
        print(f'Row count: {rowcount}')
        print(','.join(noheader))
        print('\n')
        
