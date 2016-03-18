#this prints a list of all the words in a file with the number of times it appears
file_name = raw_input('Enter file:')
if len(file_name) < 1 : file_name = "prob.txt"
handle = open(file_name,'r')
text = handle.read()
words = text.split()
Words=[]

for line in words:
    Words.append(line.strip())
print "# of words in doc:"
print len(Words)

