import csv
from math import sqrt
from random import randint
files = {
    'custom.csv':',',
    }
for file, delimeter in files.items():
    with open(file, 'wt',  newline='') as table:
        write = csv.writer(table, escapechar='\\')
        write.writerow(('abc','cbac','dga'))
        for x in range(100):
            random_string = ''.join(chr(randint(65, 90)) for _ in range(4))
            row = (x + 3.14, x / 100 + sqrt(225 + x), random_string)
            write.writerow(row)
            print(x)
for file, delimeter in files.items():
    with open(file, 'r') as table:
        text = csv.reader(table, delimiter=delimeter, skipinitialspace=True)
        for x in text:
            print(','.join(x))
        
