"""TUPLES ARE LIKE LISTS
-tuples are another kind of sequence that function
much like a list-they have elements which are indexed
starting at 0.
A tuple is a nonchangeable list!!!!!
"""

x = ('Glenn', 'Sally', 'Joseph')
print x[2]
#Joseph
y = (1,9,2)
print y
#(1, 9, 2)
print max(y)
#9
for iter in y:
    print iter
#1
#9
#2

"""
...BUT TUPLES ARE 'IMMUTABLE'
-unllike a list, once you create a tuple, you
cannot alter its contents-similar to a string
"""
x = [9,8,7]
x[2]=6
print x
#[9, 8, 6]
#list is mutable, 3rd item
#changed from 7 to 6

"""y = 'ABC'
y[2] = 'D'
#string-"traceback"

z = (5,4,3)
z[2]=0
#traceback, not mutable
"""
"""THINGS NOT TO DO WITH TUPLES
x.sort()
x.append()
x.reverse()

A TABLE OF 2 SEQUENCES
1 = list()
dir(1)
['append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

t = tuple()
dir(t)
"""

"""TUPLES ARE MORE EFFICIENT
-since Python does not have to build tuple
structures to be modifiable, they are simpler
and more efficient in terms of memory use and performance
than lists.
-so in our program when we are making 'temporary
variables' we prefer tuples over lists.
-we use tuples if we are going to use lists that
never change!!!!

TUPLES AND ASSIGNMENT
-we can also put a tuple on the left hand side of
an assignment statement
-we can even omit the parenthesis
-can't have constants on the left hand side
-can have constants or strings on the right hand side
"""

(x,y) = (4,'fred')
print y
#fred
(a,b) = (99,98)
print a
#99
a,b = (99,98)
print a
#99

"""
TUPLES AND DICTIONARIES
-the items() method in dictionaries
returns a list of (key,value) tuples
"""

d = dict()
d['csev'] = 2
d['cwen'] = 4
for (k,v) in d.items():
    print k,v
#csev 2
#cwen 4
    
tups=d.items()
print tups
#[('csev', 2), ('cwen', 4)] #this is a list of 2 tuples, key + value

    
anita=d.items()
print anita

"""
TUPLES ARE COMPARABLE
-the comparison operators work with tuples
and other sequences if the first item is equal,
Python goes on to the next element, and so on,
until it finds the elements that differ
"""

(0,1,2)<(5,1,2)
#true
(0,1,2000000)<(0,3,4)
#true
('Jones','Sally')<('Jones','Fred')
#false--j is equal to j but S is not less than F so it is false
('Jones','Sally')>('Adams','Sam')
#true


"""
SORTING LISTS OF TUPLES
-we can take advantage of the ability
to sort a list of tuples to
get a sorted version of a dictionary.
-1st we sort the dictionary by the key
using the items() method.
#10 min in
"""

d = { 'a' :10, 'b': 1,'c': 22}
t = d.items()
print t
#[('a', 10), ('c', 22), ('b', 1)]
t.sort()
print t
#[('a', 10), ('b', 1), ('c', 22)]


dictionar = { 'a' :10, 'b': 1,'c': 22}
t = dictionar.items()
print t
#[('a', 10), ('c', 22), ('b', 1)]
t.sort()
print t
#[('a', 10), ('b', 1), ('c', 22)]

"""USING sorted()
-we can do this even
more directly using the built-in
function sorted that takes a
sequence as a parameter and
returns a sorted sequence.
"""

d = { 'a' :10, 'b': 1,'c': 22}
t = d.items()
#[('a', 10), ('c', 22), ('b', 1)]

t = sorted(d.items())
print t
#[('a', 10), ('b', 1), ('c', 22)]

for k, v in sorted(d.items()):
    print k, v
#a 10
#b 1
#c 22


#13 min in
"""
SORT BY VALUES INSTEAD OF KEY
-if we could construct a list of tuples
of the form (value,key) we could sort
by  value.
-we do this with a 'for' loop that
creates a list of tuples
"""

c = { 'a' :10, 'b': 1,'c': 22}
tmp = list()
for k, v in c.items():
    tmp.append( (v,k) )
print tmp
#[(10, 'a'), (22, 'c'), (1, 'b')]
#tmp is a temporary value, a temporary list
#we are appending to create a tuple, a list of 2 tuples
#value first,key second

tmp.sort(reverse=True)
print tmp
#[(22, 'c'), (10, 'a'), (1, 'b')]


#THE 10 MOST COMMON WORDS
fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1

lst = list()
for key, val in counts.items():
    lst.append(  (val,key)  )

lst.sort(reverse=True)

for val, key in lst[:10] :
    print key,val

#THE ANSWER
"""
the 3
is 3
and 3
sun 2
yonder 1
with 1
window 1
what 1
through 1
soft 1
"""

"""EVEN SHORTER VERSION (adv)
-list comprehension creates a dynamic
list.  In this case, we make a list of
reversed tuples and then sort it.

http://wiki.python.org/moin/HowTo/Sorting"""

c = { 'a' :10, 'b': 1,'c': 22}

print sorted ( [(v,k) for k,v in c.items() ] )
print c

#[(1, 'b'), (10, 'a'), (22, 'c')]
#{'a': 10, 'c': 22, 'b': 1}

"""SUMMARY
-TUPLES ARE LIKE LISTS BUT YOU CAN'T CHANGE THEM!
-tuple syntax
mutability(not)
-comparability
-sortable
-tuples in assignment statements
-tuples in functions(adv)'
using sorted()
-sorting dictionaries by either key or value
"""

