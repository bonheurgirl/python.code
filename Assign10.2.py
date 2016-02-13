"""
10.2 Write a program to read through the
mbox-short.txt and figure out the distribution
by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line
by finding the time and then splitting the string
a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour,
print out the counts, sorted by hour as shown below.
Note that the autograder does not have support
for the sorted() function.

GIVEN CODE:

name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

DESIRED OUTPUT:
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1
"""
#code submitted for grade
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
days = dict()
time =  dict()
counts = dict()
hourcount = list()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From:'):
        pass
        if line.startswith('From') :
            sender = line.split()
            time = sender[5]
            hours,mins,secs = time.split(':')
            for hour in hours:
                pass
            hourcount.append(hours)
for hours in hourcount:
    if hours not in counts:
        counts[hours] = 1
    else:
        counts[hours] = counts[hours] + 1

for key, val in counts.items():
    hourcount.append(  (val,key)  )

t = counts.items()
t = sorted(counts.items())
for k, v in sorted(counts.items()):
    print k,v


#2ndcode submitted for grade without using sorted method
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
days = dict()
time =  dict()
counts = dict()
hourcount = list()

for line in fh:
    line = line.rstrip()
    if not line.startswith('From:'):
        pass
        if line.startswith('From') :
            sender = line.split()
            time = sender[5]
            hours,mins,secs = time.split(':')
            for hour in hours:
                pass
            hourcount.append(hours)
            hourcount.sort()

for hours in hourcount:
    if hours in counts:
        counts[hours] = counts[hours] + 1
    else:
        counts[hours] = 1
#print hourcount, counts
#hourcount is a list
#counts is a dictionary

t = counts.items()
print 't',t
t.sort()
#print 'sorted t',t

for key, val in t:
    hourcount.append(  (key,val)  )
    print key,val
