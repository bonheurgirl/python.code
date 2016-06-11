"""
import csv
with open('eggs.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print ', '.join(row)



import csv
with open('eggs.csv', newline=' ') as f:
    reader = csv.reader(f)
    for row in reader:
        print (row)



import sys

if sys.version_info[0] == 2:  # Not named on 2.6
    access = 'wb'
    kwargs = {}
else:
    access = 'wt'
    kwargs = {'newline':''}

with open('eggs.csv', access, **kwargs) as csv_file:
    writer = csv.DictWriter(csv_file, ['header1', 'header2'])
    writer.writeheader()
    for item in items:
        writer.writerow(item)



import csv
with open('eggs.csv', 'w') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=['header1', 'header2'], lineterminator='\n')
    writer.writeheader()
    for item in items:
        writer.writerow(item)

import csv
with open('eggs.csv', 'wb') as csv_file:
    writer = csv.DictWriter(csv_file, ['header1', 'header2'])
    writer.writeheader()
    for item in items:
        writer.writerow(item)


import csv
with open(eggs.csv','r') as f:
  with open('n.csv','w') as new_file:
    file_read = csv.reader(f,delimiter=',')
    for row in file_read:
      if not extract_n(row):
        new_file.write(row)
"""

#tab delimited file
import csv
with open('eggs.csv', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        if "n" in row:
            print(row)


import csv
with open('eggs.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        if "n" in row:
            print(row)