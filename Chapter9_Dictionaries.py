#Chapter 9 Dictionaries

"""
A collection is nice because we can put more than one value in them and
carry them all around in 1 convenient package.

We have a bunch of values in a single 'variable'

We do this by having more than one place 'in' the variable.

We have ways of finding the different places in the variable.

What is not a 'Collection'?
Most of our variables have one value in them--when we put a new
value in the variable--the old value is over written.
"""

x=2
x=4
print x

"""A story of 2 Collections...

List: A linear collection of values that stay in order. think pringles.
Dictionary: A 'bag' of values, each with its own label. think a purse.

Key value
key is the label.
The value is the thing.

Dictionaries:
-dictionaries are python's most powerful data collection
-dictionaries allow us to do fast database-like operations in python
-dictionaries have different names in different languages

Associative Arrays: Perl/Php
Properties or Map or HashMap: Java
Property Bag: C#/.Net (C sharp)

-Lists index their entries based on the position in the list.
-Dictionaries are like bags-no order.
-So we index the things we put in the dictionary with a 'lookup tag'.
"""

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print purse
#{'money': 12, 'tissues': 75, 'candy': 3}
print purse['candy']
#3
purse['candy'] = purse['candy'] + 2
print purse
#{'money': 12, 'tissues': 75, 'candy': 5}


"""
Comparing Lists & Dictionaries

-Dictionaries are like Lists except they use keys instead of numbers to look up values.
"""
lst = list()
lst.append(21)
lst.append(183)
print lst
#[21, 183]
lst[0] = 23
print lst
#[23, 183]


ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print ddd
#{'course': 182, 'age': 21}
ddd['age'] = 23
print ddd
#{'course': 182, 'age': 23}


"""Many Counters with a Dictionary
-One common use of a dictionary counting how often we 'see' something.
"""

ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print ccc
#{'csev': 1, 'cwen': 1}
ccc['cwen'] = ccc['cwen'] + 1
print ccc
#{'csev': 1, 'cwen': 2}


"""DICTIONARY TRACEBACKS

-It is an error to reference a key which is not in the dictionary.
-We can use the in operator to see if a keay is in the dictionary.
"""
"""
ccc = dict()
print ccc['csev']
#traceback
print 'csev' in ccc
#False
"""

"""WHEN WE SEE A NEW NAME

-when we encounter a new name, we need to add a new entry in the
dictionary and if this the second or later time we have seen
the name, we simply add one to the count in the dictionary under
that name
"""

counts = dict()
names = ['csev','cwen','csav','zqian','cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print counts
#{'csev': 1, 'zqian': 1, 'csav': 1, 'cwen': 2}
#19 min in

fh = open('babynames.txt','r')
baby = dict()
girls = ['hannah','michelle']
for line in fh:
    girls = line.split()
for name in girls:
    if name not in baby:
        baby[name] = 1
    else :
        baby[name] = baby[name] + 1
print baby

for girls in baby:
    print girls, baby

"""THE GET METHOD FOR DICTIONARY

This pattern of checking to see if a key is already in a
dictionary and assuming a default value if the key is not
there is so common, that there is a method called
get() that does this for us.

Default value if key does not exist(and no Traceback.)"""




if name in counts:
    print counts[name]
else:
    print 0
print counts.get(name,0)


"""SIMPLIFIED COUNTING WITH GET()
-We can use get() and provide a default value of zero when the key
is not yet in the dictionary-and then just add one-
"""  

counts = dict()
names = ['csev','cwen','csav','zqian','cwen']
for name in names:
        counts[name] = counts.get(name,0) + 1
print counts

"""COUNTING PATTERN
-THE GENERAL PATTERN TO COUNT THE WORDS IN A LINE OF TEXT
IS TO SPLIT THE LINE INTO WORDS, THEN LOOP THROUGH THE WORDS
AND USE A DICTIONARY TO TRACK THE COUNT OF EACH WORD
INDEPENDENTLY."""
counts = dict()
print 'Enter a line of text:'
line = raw_input(")

words = line.split()
print 'Words:',words

print 'Counting...'
for word in words:
    counts[word] = counts.get(word,0) + 1

print 'Counts',counts

#25 min

"""DEFINITE LOOPS AND DICTIONARIES
-Even though dictionaries are not stored in order,
we can write a for loop that goes through all the entries
in a dictionary-actually it goes through all of the keys
in the dictionary and looks up the values.
"""

counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print key, counts[key]

#jan 100
#chuck 1
#fred 42

counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print key, counts[key]
print counts.values()
#[100, 1, 42]

"""RETRIEVING LISTS OF KEYS & VALUES
-You can get a list of keys, values
or items (both) from a dictionary.
"""
jjj = {'chuck': 1,'fred': 42,'jan':100}
print list(jjj)
                 #['jan', 'chuck', 'fred']
print jjj.keys()
                 #['jan', 'chuck', 'fred']
print jjj.values()
                 #[100, 1, 42]
print jjj.items()
                 #[('jan', 100), ('chuck', 1), ('fred', 42)]
                 #THIS IS A TUPLE
                 # A TUPLE IS A KEY,VALUE PAIR
                 #THIS WORKS BEAUTIFULLY ON A FOR LOOP

"""BONUS: 2 ITERATION VARIABLES!
-we loop through the key-value pairs in a
dictionary using 2 iteration variables.
-each iteration, the 1st variable is the key
and the 2nd variable is the corresponding
value for the key."""

jjj = {'chuck': 1,'fred': 42,'jan':100}
for aaa,bbb in jjj.items():
    print aaa,bbb

#jan 100
#chuck 1
#fred 42

#this program counts the most common word in a file
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
print bigword,bigcount

#SUMMARY OF CHAPTER 9
"""
What is a collection?
Lists versus Dictionaries
Dictionary constants
The most common word
Using the get() method
HAshing, and lack of order
Writing dictionary loops
Sneak peek:tuples
Sorting dictionaries

An empty pair of curly braces {} 
is an empty dictionary, just like
an empty pair of [] is an empty list.

The length len() of a dictionary 
is the number of key-value pairs 
it has. Each pair counts only once, 
even if the value is a list. (That's
right: you can put lists inside 
dictionaries!)



