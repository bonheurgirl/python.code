"""The Regular Expression Module
-Before you can use regular expressions
in your program, you must import the
library using 'import re'
-You can use re.search() to see if a
string matches a regular expression
similar to using the find() method for
strings
-You can use re.findall() extract portions
of a string that match  your regular
expression similar to a combo of find()
and slicing: var[5:10]"""


"""USING re.search() like find()"""

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:')>=0:
        print line

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:',line):
        print line
        
        
"""Using re.search() like startswith()"""

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:'):
        print line

import re
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:',line):
        print line
#we fine-tune what is matched by adding
special characters to the string.

WILD-CARD CHARACTERS
-the dot character matches any character
-if you add the asterisk character, the
character is 'any number of times'
^X.*:

FINE-TUNING YOUR MATCH
-depending on how 'clean' your data is and
the purpose of your appliction, you may 
want to narrow your match down a bit.

^X-\S+: 

MATCHING AND EXTRACTING DATA
-The re.search() returns a True/False
depending on whether the string
matches the regular expression.
-If we actually want the matching strings
to be extracted, we usee re.findall().

import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print y
#+ is one or more digits
#['2', '19', '42']

y = re.findall('[AEIOU]+',x)
print y
#[]

WARNING: GREEDY MATCHING
-The repeat characters (* and +) push
outward in both directions (greedy)
to match the largest possible string.

import re
x = 'From: Using the :character'
y = re.findall('^F.+:',x)
print y
^F.+:   ^F==1st character in the match is an F
        .+==one or more characters
        :==last character in the match is a :

NON-GREEDY MATCHING
-Not all regular expression
repeat codes are greedy! IF you 
add a ? character - the + and
* chill out a bit...

import re
x = 'From: Using the :character'
y = re.findall('^F.+?:',x)
print y
^F.+?:   ^F==1st character in the match is an F
        .+==one or more characters but not greedily
        :==last character in the match is a :
#['From:']
#18 min in

