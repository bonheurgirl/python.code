#READING FILES

"""OPENING A FILE
open() returns a file handle
handle = open(filename,mode)
fhand = open('mbox.txt','r')

mode is optional an should be 'r' if we are planning reading
the file and 'w' if we are going to write to the
file.
"""

fhand = open('mbox.txt','r')



#THE NEWLINE CHARACTER
#WE USE A SPECIAL CHARACTER TO INDICATE WHEN A LINE
#ENDS CALLED THE 'NEWLINE'  
#WE REPRESENT IT AS \n in strings

stuff = 'Hello\nWorld!'
print stuff

stuff = 'X\nY'
print stuff

len(stuff)
print len(stuff)

"""File Handle as a Sequence

xfile = open('mbox.txt')
for cheese in xfile:
    print cheese
    (these 3 lines open a file and reads
    every line in the file)
    
"""

#COUNTING LINES IN A FILE
#open it, write a for loop, and add count+1

fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
    
print 'Line Count:',count


#READING THE WHOLE FILE
fhand = open('mbox-short.txt')
inp = fhand.read()
print len(inp)

print inp[:20]

#SEARCHING THROUGH A FILE
"""We can put an if statement in out for loop
to only print lines that meet ome criteria"""

fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:') :
        print line
        
"""the print statement adds a newline
to each line.  each line from the file also has
a newline at the end.  We can strip the whitespace
from the right hand side of the string
using rstrip() from the string library.
The newline is considered "white space" and
is stripped."""

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:') :
        print line
        
        
"""SKIPPING WITH CONTINUE
We can conveniently skip a line by using the 
continue statement."""

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    #Skip 'uninteresting lines'
    if not line.startswith('From:') :
        continue
    #Process our 'interesting' line
    print line
        
"""USING 'IN' TO SELECT LINES.
We can look for a string anywhere in a line 
as our selection criteria."""

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.az.za' in line:
        continue
    print line
    """Skips all the lines that don't have
    this string '@uct.az.za' in it."""
    
"""PROMPT FOR FILE NAME"""
fname = raw_input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print 'There were',count, 'subject lines in',fname


#BAD FILE NAMES

name = raw_input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print 'File cannot be opened:',fname
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print 'There were',count, 'subject lines in',fname

