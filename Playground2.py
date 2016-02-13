
count = 0
fh = open('mbox-short.txt','r')
for line in fh:
    line = line.rstrip()
    if line.startswith('From:') :
        print line
        count = count + 1
#print count
        
print "There were", count, "lines in the file with From as the first word"

