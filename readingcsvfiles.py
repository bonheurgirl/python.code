import csv
with open('sleepdataCopy.csv', 'rb') as csvfile:
    filereader = csv.reader (csvfile,  delimiter =' , ', quotechar= ' | ')
    for row in filereader:
        print ' , ' .join(row)
