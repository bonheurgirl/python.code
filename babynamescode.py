#lists all the names in the file and gives a count
"""fh = open('babynames.txt','r')
baby = dict()
girls = []
for line in fh:
    girls = line.split()
for name in girls:
    if name not in baby:
        baby[name] = 1
    else :
        baby[name] = baby[name] + 1
print baby

for girls in baby:
    #print girls, baby
    continue

"""


fh = open('GA.Practice.Program.py','r')
program = dict()
all_words=[]

for line in fh:
    all_words = line.split()
    
for word in all_words:
    if word not in all_words:
        program[word] = 1
    else:
        program[word] = program[word] + 1
print program