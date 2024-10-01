import csv
import random
import string
files = {
    'custom2.csv':',',
    }
num_lists = 25        
list_size = 4        
listf = [] #gen list of lists
for _ in range(num_lists):
    inner_list = []  
    for _ in range(list_size):
        random_length = random.randint(1, 10)  
        random_string = ''.join(random.choices(string.ascii_uppercase, k=random_length))
        inner_list.append(random_string)
    listf.append(inner_list)
for file, delimeter in files.items():
    with open(file, 'wt',  newline='') as table:
        write = csv.writer(table, escapechar='\\')
        write.writerows(listf)
for file, delimeter in files.items():
    with open(file, 'r') as table:
        text = csv.reader(table, delimiter=delimeter, skipinitialspace=True)
        for x in text:
            print(','.join(x))
