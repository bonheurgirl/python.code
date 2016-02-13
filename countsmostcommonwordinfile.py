"""#this program counts the most common word in a file
name = raw_input('Enter file:')
handle = open(name,'r')
text = handle.read()
words = text.split()

counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print "the most common word is",bigword,"and it appears", bigcount, "times."
"""

#I want to create program that will catalog all words in a file
name = raw_input('Enter file:')
if len(name) < 1 : name = "babynames.txt"
handle = open(name,'r')
text = handle.read()
words = text.split()

counts = dict()
for word in words:
    counts[word] = counts.get(word,0) + 1
print words

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print "the most common word is",bigword,"and it appears", bigcount, "times."


