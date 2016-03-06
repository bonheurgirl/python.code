"""
try:
    name = raw_input ("What is your name?")
    inp = raw_input ("Enter how much do you love Anita from 1 through 10!")
    love = float(inp)
    inp = raw_input ("Enter how much do you love yourself from 1 through 10!")
    you = float(inp)
except:
    print 'Please enter numeric input'
    print 'What are you waiting for?'
    break


if you > 5 :
    print 'You need Anita!'
else :
    print 'Maybe you should invest in some therapy!'


if love  >= 9 :
    print 'Not even close'
elif love >= 8 :
    print 'Who are you kidding'
elif love >= 5 :
    print 'Seriously'
elif love >= 4 :
    print 'Getting better, but not high enough'
elif love >= 3 :
    print 'You suck'
else :
    print ''

print "Well", name
print "Anita loves herself more!"
    
    


You can do

try:
   #whatever function 
except:
   pass
This lets any exception "pass" without any interruptions.

Or if you want to get True or False returned from a function you can do something like

def isexcept():
    try:
       #whatever function 
       #if execution succeeds 
       return True
    except:
       return False


from __future__ import division
score = int((25/26) * 100)
print score,"%","score achieved" 


correctanswers=104
incorrectanswers=27
total=correctanswers+incorrectanswers

print "The total number of questions were", total
print "Number of Correct Answers:", correctanswers
print "Number of Wrong Answers:", incorrectanswers

score = int((correctanswers/total) * 100)

print score,"%","score achieved" 

#print int((correctanswers/26) * 100),"%", "score achieved"

if score >= 78:
    print "Congratulations, You are ready to take the Google Analytics IQ Certification Exam."
else:
    print "You may want to complete more practice questions before attempting the  Google Analytics IQ Certification Exam."
    
    
    
print "Thank you for completing the Google Analytics Practice Program."
print "Have a nice day & good luck"
"""

#TRYING OUT A SKIP STATEMENT

from __future__ import division
print
print"""G6. Setting up goals allows you to see________.

a) bounce rate
b) conversion rates
c) a list of transactions
d) ecommerce revenue"""

correctanswers=130
incorrectanswers=10
skipped=5
total=(correctanswers+incorrectanswers) - skipped

g6 = raw_input("Please enter your answer: ")

if g6 == "b" or g6 == "B":
    print "correct!"
    correctanswers = correctanswers + 1
    
elif g6=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is ."
    incorrectanswers = incorrectanswers + 1

print "The total number of questions were", total
print "Number of Correct Answers:", correctanswers
print "Number of Wrong Answers:", incorrectanswers
print "Number of Skipped Questions:", skipped

score = int((correctanswers/total) * 100)

print score,"%","score achieved" 