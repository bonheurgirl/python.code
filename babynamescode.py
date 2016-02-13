fh = open('babynames.txt','r')
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

