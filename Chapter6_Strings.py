#String Data Type
#a string is a sequence of characters
#for strings, + means "concatenate"
#when a string contains numbers, it is still a string
# we can convert numbers in a string into a number using int()

str1 = "Hello"
str2 = 'there'
bob = str1 + str2
print bob

str3 = '123'
x = int(str3) + 1
print x

#READING AND COVERTING
#raw input takes a string and places it into a variable
name = raw_input('Enter:')
print name

apple = raw_input('Enter:')
#Enter: 100
#x = apple - 10
# traceback error
x = int(apple) - 10
print x

#LOOKING INSIDE STRINGS
#SQUARE BRACKETS, THE INDEX VALUE MUST BE AN INTEGER AND STARTS AT ZERO
fruit = 'banana'
letter = fruit[1]
print letter

n = 3
w = fruit[n - 1]
print w

#STRINGS HAVE LENGTH/len function is a built in function
fruit = 'banana'
print len(fruit)

#LOOPING THROUGH STRINGS
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print index,letter
    index = index + 1
    
fruit = 'banana'
for letter in fruit:
    print letter
    
    
#LOOPING AND COUNTING
#PRINTS OUT THE NUMBER OF A'S IN BANANA
word = 'banana'
count = 0
for letter in word :
    if letter =='a' :
        count = count + 1
print count

#LOOKING DEEPER INTO 'IN'
#THE ITERATION VARIABLE INTERATES THROUGH THE SEQUENCE

for letter in 'banana' :
    print letter
    
#SLICING STRINGS
#THE SECOND NUMBER IS ONE BEYOND THE END OF THE SLICE
#'UP TO BUT NOT INCLUDING'
#IF THE 2ND NUMBER IS BEYOND THE END OF THE STRING,
#IT STOPS AT THE END
s = 'Monty Python'
print s[0:4]
print s[6:7]
print s[6:20]
#IF WE LEAVE OFF THE FIRST NUMBER OR THE LAST NUMBER OF THE SLICE.
#IT IS ASSUMED TO BE THE BEGINNING OR END OF THE STRING RESPECTIVELY
s = 'Monty Python'
print s[:2]
print s[8:]
print s[:]

#STRING CONCATENATION
a = 'hello'
b = a + 'There'
print b
c = a + " + " 'There'
print c


#using 'in' as an operator
#the 'in' keyword can also be used to check to see if one string is in another string

fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit:
    print 'Found it!'

#STRING LIBRARY
greet = 'Hello Bob'
zap = greet.lower()
print zap
print greet
print 'Hi There'.lower()

dir(stuff)

#SEARCHING A STRING
#WE USE THE find() function to search for a substring within another string


#MAKING EVERYTHING UPPER CASE (20MIN IN)
greet = 'Hello Bob'
nnn = greet.upper()
print nnn
#HELLO BOB

www = greet.lower()
print www
#hello bob


#SEARCH AND REPLACE
#The replace() function is like a "search and replace"
#operation in a word processor

greet = 'Hello Bob'
nstr = greet.replace('Bob','Jane')
print nstr

greet = 'Hello Bob'
nstr = greet.replace('o','X')
print nstr

#STRIPPING WHITESPEACE
#Sometimes we want to take a string and remove
#whitespace at the beginning and/or end
#lstrip() and rstrip() to the left and right only
#strip() removes both begin and ending whitespace

greet = ' Hello Bob '
greet.lstrip()

greet.rstrip()

greet.strip()

#PREFIXES
line = 'Pkease have a nice day'
line.startswith('Please')
line.startswith('p')

#PARSING TEXT
