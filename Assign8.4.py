"""
#“Write a program to open the file romeo.txt and read it 
line by line. For each line, split the
line into a list of words using the split function. 
For each word, check to see if the word is
already in a list. If the word is not in the list,
add it to the list. 
When the program completes, sort and print the
resulting words in alphabetical order. 
Enter file: romeo.txt 
[’Arise’, ’But’, ’It’, ’Juliet’, ’Who’, ’already’,  ​
 ’and’, ’breaks’, ’east’, ’envious’, ’fair’, ’grief’,  ​ 
’is’, ’kill’, ’light’, ’moon’, ’pale’, ’sick’, ’soft’, 
 ’sun’, ’the’, ’through’, ’what’, ’window’,  ​ ’with’, 
’yonder’]”


"""
#THIS IS THE CODE SUBMITTED FOR GRADE
fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.rstrip().split()
    #print words
    for word in words:
        if word in lst:
            continue 
        else: 
            lst.append(word)
            lst.sort()          
print lst
 



##this code works but does not use append function
with open('romeo.txt','r') as f:    # open your file and auto close it
    uniq=set()         # a set only has one entry of each
    for line in f:     # file line by line
        for word in line.split():    # line word by word
            uniq.add(word)           # uniqueify by adding to a set

print sorted(uniq)  
"""


#fname = raw_input("Enter file name: ")
fhand = open('romeo.txt','r')
lst = list()
for line in fhand:
    words = line.rstrip().split()
    for word in words:
        lst.append(word) 
        lst.sort()

print "updated list:",lst
    

    
