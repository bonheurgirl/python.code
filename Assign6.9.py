#WRITE SOME CODE TO PARSE LINES OF THE FORM:

#X=DSPAM-Confidence: 0.8475
#Use find and string slicing to extract the portion of the string
#after the colon character and then use the float function to
#convert the extracted string into a floating point number.

data = 'X=DSPAM-Confidence: 0.8475'
print data
firstpos = data.find(':')
print firstpos
print data[firstpos + 1:]
num = float(data[firstpos+1:])
print num, type(num)

"""
sppos = data.find('5',atpos)
print sppos

extraction = data[atpos + 1 :sppos + 1]
print extraction

extraction = float(data[20:26])
print extraction
"""

data = 'X=DSPAM-Confidence: 0.8475'
print data
firstpos = data.find(':')
print firstpos
print data[firstpos + 1:]
num = float(data[firstpos+1:])
print num


#ASSIGNMENT, GRADED

data = "X-DSPAM-Confidence:    0.8475";

firstpos = data.find(':')


num = float(data[firstpos+1:])
print num