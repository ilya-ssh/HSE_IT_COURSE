import csv
files = {
    'tempquotes.csv':'|',
    }
for file, delimeter in files.items():
    with open(file, 'r') as table:
        text = csv.reader(table, delimiter=delimeter, skipinitialspace=True, quoting=csv.QUOTE_ALL)
        for x in text:
            print(','.join(x))
