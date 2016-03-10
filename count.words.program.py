file_name = raw_input('Enter file:')
if len(file_name) < 1 : file_name = "GA.Practice.Program.py"
handle = open(file_name,'r')
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
print "the most common word is(",bigword,")and it appears", bigcount, "times."