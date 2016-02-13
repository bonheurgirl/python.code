"""
import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print y
#+ is one or more digits

y = re.findall('[AEIOU]+',x)
print y

import re
x = 'From: Using the :character'
y = re.findall('^F.+?:',x)
print y

"""


def miles_to_feet():
    mileage = int(float(input('Enter miles:')))
    feet = mileage * 5280
    return feet
print miles_to_feet()

string_1 = "Camelot"
string_2 = "place"
print "My name is %s. 'Tis a silly %s." % (string_1, string_2)


