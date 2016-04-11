"""
import sys

def write():
    print('Creating new text file') 

    name = raw_input('Enter name of text file: ')+'.txt'  # Name of text file coerced with +.txt

    try:
        file = open(name,'a')   # Trying to create a new file or open one
        file.close()

    except:
        print('Something went wrong! Can\'t tell what?')
        sys.exit(0) # quit Python

write()


file_name = raw_input('Enter file:')
if len(file_name) < 1 : file_name = "subtitle.txt"
handle = open(file_name,'r')

text = handle.read()
text = text.rstrip()
#print text

with open(text) as f:
    data=f.readlines()
f = open('subtitle.text','w')
f.write(data + '\n')
f.close()
print data


# Open the file for reading.
with open('subtitle.txt', 'r') as infile:

    data = infile.read()  # Read the contents of the file into memory.
# Return a list of the lines, breaking at line boundaries.
my_list = data.splitlines()
print my_list

for line in open("subtitle.txt") :
    print line.rstrip('\n') # .rstrip('\n') removes the line break
    
for line in open("subtitle.txt"):
    print line.rstrip()
"""    

file_name = raw_input('Enter file:')
max(open(file_name), key=len)
print len

