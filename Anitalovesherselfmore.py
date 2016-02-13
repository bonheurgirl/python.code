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
    
    
"""

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
"""

