#code submitted for grade
name = raw_input("Enter file:")
if len(name) < 1 : name = "Final_Quiz.txt"
fh = open(name)
print fh

for line in fh:
    line = ' '.join(line.split())
print fh
print line
