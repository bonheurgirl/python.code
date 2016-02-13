print "The %s who %s %s!" % ("Knights", "say", "Ni")
# This will print "The Knights who say Ni!"

count = 0
sum = 0
friends = [ 'Joseph', 'Glenn', 'Sally' ]
print len(friends)
print friends[2]
count = count + 1
sum = sum + count
print "count:", count
print "sum:", sum


data = ['x']
print len(data)


a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print len(c)
print range(len(c))


t = [9, 41, 12, 3, 74, 15]
print t[:]
print t[2:4]

friends = [ 'Joseph', 'Glenn', 'Sally' ]
friends.sort()
print friends[0]


fhand = open('romeo.txt','r')
lst = list()
for line in fhand:
    words = line.rstrip().split()
    for word in words:
        if word in lst:
            continue
        if word not in lst:
            lst.append(word) 
            lst.sort()

print lst
