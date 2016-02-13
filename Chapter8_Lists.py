"""A LIST IS A KIND OF COLLECTION
* A COLLECTION ALLOWS US TO PUT MANY VALUES IN A SINGLE
'VARIABLE'
* A COLLECTION IS NICE BECAUSE WE CAN CARRY ALL MANY
VALUES AROUND IN 1 CONVENIENT PACKAGE. """

friends = ['Joseph','Glenn','Sally']

carryon = ['socks','shirt','perfume']

"""What is NOT a collection"""

x = 2
x = 4
print x
# 4

"""LIST CONSTANTS
List constants are surrounded by square brackets
and the elements in the list are separated by
commas.

A list element can be any Python object--even 
another list

A list can be empty"""

print [1,24,76]
print ['red','yellow','blue']
print ['red',24,98.6]
print [1, [5,6], 7]
print []

"""LOOKING INSIDE LISTS

Just like strings, we can get any single element
in a list using an index specified in square
brackets.

The first item in a list is sub O, sub 1, sub 2...
"""

friends = ['Joseph','Glenn','Sally']
print friends[1]

"""LISTS ARE MUTABLE...STRINGS ARE NOT (CHANGEABLE)

Strings are 'immutable'-we cannot change the
contents of a string-we must make a new string
to make any change

Lists are 'mutable'-we can change an element
of a list using the index operator."""

fruit = 'Banana'
#fruit[0] = 'b'
#traceback error

x=fruit.lower()
print x

lotto = [2,14,26,41,63]
print lotto
lotto[2] = 28
print lotto
#[2,14,28,41,63]


"""How long is a list?

The len() function takes a list as a parameter
and returns the number of elements in the list.

Actually len() tells us the number of
elements of any set or sequence (i.e. such as
a string...)"""

greet = 'Hello Bob'
print len(greet)
#9

x= [1,2,'joe',99]
print len(x)
#4

"""USING THE RANGE FUNCTION

The range function returns a list of numbers
that range from zero to one less than the 
parameter.  It creates a list and gives it to us
back.

We can construct an index loop using 'for'
and an integer interator."""

print range(4)
#[0,1,2,3,]

friends = ['Joseph','Glenn','Sally']
print len(friends)
#3

print range(len(friends))
#[0,1,2]


#A tale of 2 loops (they both produce the same output)
friends = ['Joseph','Glenn','Sally']
for friend in friends:
    print 'Happy New Year:', friend
    #this loop is preferred!!!!!!!!
    
for i in range(len(friends)):
    friend = friends[i]
    print 'Happy New Year:', friend
    
print len(friends)
print range(len(friends))
#[0,1,2]


"""CONCATENATING LISTS USING +
WE CAN CREATE A NEW LIST BY ADDING
2 EXISTING LISTS TOGETHER"""
a = [1,2,3]
b = [4,5,6]
c = a + b
print c
print a

"""LISTS CAN BE SLICED USING ':'
REMEMBER: JUST LIKE IN STRINGS, THE
2ND NUMBER IS 'UP TO BUT NOT 
INCLUDING'
"""
#    0 1  2  3  4  5
t = [9,41,12,3,74,15]
t[1:3]
#[41,12]
t[:4]
#[9,41,12,3]
t[3:]
#[3,74,15]
t[:]
#[9,41,12,3,74,15]

t = [9,41,12,3,74,15]
print t[1:3]
print t[:4]
print t[3:]
print t[:]

"""LIST METHODS"""
X = list()
type(x)
dir(x)
append, count, extend, index, insert, pop,
remove, reverse, sort


"""BUILDING A LIST FROM SCRATCH

WE CAN CREATE AN EMPTY
LIST AND THEN ADD ELEMENTS USING THE
APPEND METHOD.

THE LIST STAYS IN ORDER AND NEW ELEMENTS
ARE ADDED AT THE END OF THE LIST"""

stuff = list()
stuff.append('book')
stuff.append(99)
print stuff

stuff.append('cookie')
print stuff

12 min in
"""IS SOMETHING 'IN' A LIST?

Python provides 2 operators that let you
check if an item is in a list.

These are logical operators that return
True or False.
They do not modify the list.
"""
some = [1,9,21,10,16]
9 in some
15 in some
20 in some

"""A LIST IS AN ORDERED SEQUENCE

A list can hold many items and keeps
those items in the order until we do
something to change the order.

A list can be sorted (i.e. change its
order)

The sort method (unlike in strings) means
'sort yourself'."""

friends = ['Joseph','Glenn','Sally']
friends.sort()  #it put the list in alpha order
print friends
print friends[1]

"""BUILT IN FUNCTIONS AND LISTS

There are a number of functions built
into Python that takes lists as parameters.

Remember the loops we built?  These are much
simpler."""

nums = [3,41,12,9,74,15]
print len(nums)
print max(nums)
print min(nums)
print sum(nums)
print sum(nums)/len(nums) #this is the average

#AVERAGING WITH A LIST

total = 0
count = 0
while True:
    inp = raw_input('Enter a number: ')
    if inp =='done': break
    value = float(inp)
    total = total + value
    count = count + 1

average = total/count
print 'Average:',average


numlist = list()
while True:
    inp = raw_input('Enter a number: ')
    if inp =='done': break
    value = float(inp)
    numlist.append(value)

averae = sum(numlist)/len(numlist)
print 'Average:',average

"""BEST FRIENDS: STRINGS & LISTS

Split breaks a string into parts produces
a list of strings. We think of these as
words.  We can access a particular
world or loop through all the words."""

abc = 'With three words'
stuff = abc.split()
print stuff
# ['With', 'three', 'words']

print len(stuff)
#3
print stuff [0]
#With
print stuff
#['With', 'three', 'words']

for w in stuff:
    print w
#With
#three
#word
    
line = 'A lot            of           spaces'
etc = line.split()
print etc
#python throws away all the extra spaces 

line = 'first;second;third'
thing = line.split()
print thing
print len (thing)

thing = line.split(';')
print thing
print len(thing)
    

"""THE DOUBLE SPLIT PATTERN

Sometimes we split a line one way and then grab
one of the pieces of the line and split that
piece again."""

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
words = line.split()
email = words[1]
pieces = email.split('@')

24 min in
    
#Chapter 8 exercises.  An Example of a solution for
#exercise 8.6.
# reads numbers until the program is done and
# prints the maximum and the minimum

#while loop to append numbers to the list

working_list = list()

while True:
    # handle the edge cases
    inp = raw_input('Enter a number or "done"\n')
    if inp == "done":
        # check for empty list    
        if len(working_list) < 1:
            working_list.append("None")
        break
    # check for empty line
    if len(inp) < 1:
        if len(working_list) < 1:
            working_list.append("None")
        break
    # do the work
    try:
        num = float(inp)
    except:
        print "Invalid input"
        continue
    working_list.append(num)   

# prints results
print "The minimum is" , min(working_list)
print "The maximum is" , max(working_list) 
