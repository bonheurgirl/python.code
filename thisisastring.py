"""
x = 'this is a string'
splitted = x.split()
count = 0
while count <= len(splitted) -1:
    #print splitted[count]
    count = count + 1
#print count



"""

"""

fh = open('mbox-short.txt','r')
email = dict()
for line in fh:
    line = line.rstrip()
    if line.startswith('From:') :
        sender = line.split()
        #print sender[1:2]

        for name in sender[1:2]:
            if name not in email:
                email[name] = 1
            else :
                email[name] = email[name] + 1
for value in email:
    pass
for key in email:
    print 'email address',email [key]
                     
#print email
print 'max', max(email, key=email.get)
#NOT IT EITHER!print max(email.values(),email.keys())
# NOT IT!for key in email: print max(email)
"""

"""
fh = open('mbox-short.txt','r')
email = dict()
for line in fh:
    line = line.rstrip()
    if line.startswith('From:') :
        sender = line.split()
        #print 'Sender:', sender
        #print 'Counting...'
        for word in sender[1:2]:
          email[word] = email.get(word,0) + 1
#print 'Email', email
#print 'max', max(email, key=email.get)
for key in email:
    #print key, email[key]
for word in email.items():
    #print word
bigcount = None
bigword = None
for word,count in email.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print bigword,bigcount

"""

fh = open('mbox-short.txt','r')
email = dict()
for line in fh:
    line = line.rstrip()
    if line.startswith('From:') :
        sender = line.split()
        #print 'Sender:', sender
        #print 'Counting...'
        for word in sender[1:2]:
          email[word] = email.get(word,0) + 1
#print 'Email', email
#print 'max', max(email, key=email.get)
for key in email:
    continue
for word in email.items():
    continue
bigcount = None
bigword = None
for word,count in email.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print bigword,bigcount
