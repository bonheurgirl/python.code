# -*- coding: UTF-8 -*-
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

#this code works
import csv
with open('eggs.csv', 'rb') as f:
    reader = csv.reader(open("eggs.csv", 'rU'), dialect='excel')
    for row in reader:
        if "n" in row:
            print(row)
"""

# Load Pandas
from pandas import DataFrame

# Load each file into a pandas dataframe, this is based on a numpy array
data1 = DataFrame.from_csv('black.csv',sep=',',parse_dates=False)
data2 = DataFrame.from_csv('blue.csv',sep=',',parse_dates=False)

#Now add 'header5' from data1 to data2
data2['header15'] = data1['header15']

#Save it back to csv
data2.to_csv('output.csv')

"""
# Load Pandas
from pandas import DataFrame

# Load each file into a pandas dataframe, this is based on a numpy array
data1 = DataFrame.from_csv('oldads.csv',sep=',',parse_dates=False)
data2 = DataFrame.from_csv('newads.csv',sep=',',parse_dates=False)

#Now add 'headers' from data1 to data2
data2['header1'] = data1['header1']
data2['header3'] = data1['header21']
data2['header4'] = data1['header22']
data2['header5'] = data1['header3']
data2['header6'] = data1['header4']
data2['header10'] = data1['header7']
data2['header11'] = data1['header8']

#Save it back to csv
data2.to_csv('output.csv')
"""