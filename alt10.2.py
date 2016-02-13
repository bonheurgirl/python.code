fh = open('mbox-short.txt','r')
days = dict()
time =  dict()
counts = dict()
hourcount = list()
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith('From:'):
        pass
        if line.startswith('From') :
            sender = line.split()
            #print sender
            #print len(sender)
            #print range(len(sender))
            #print sender[5]
            time = sender[5]
            #print time
            hours,mins,secs = time.split(':')
            #print time
            #print hours
            #print hours
            for hour in hours:
                pass
            hourcount.append(hours)
#print 'hourcount', hourcount

#NEW DICTIONARY counts= dict()
#OLD DICTIONARY hourcounts=['04', '06', '07', '09', '10', '11', '14', '15', '16', '17', '18', '19']

for hours in hourcount:
    if hours not in counts:
        counts[hours] = 1
    else:
        counts[hours] = counts[hours] + 1
    #print counts

for key, val in counts.items():
    hourcount.append(  (val,key)  )
    #print key,val

t = counts.items()
t = sorted(counts.items())
#print t
for k, v in sorted(counts.items()):
    print k,v


                
