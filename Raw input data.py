name = raw_input ("What is your name?")
love = raw_input ("Enter how much do you love Anita from 1 through 10!")
you = raw_input ("Enter how much do you love yourself from 1 through 10!")
print "Well", name
print "Anita loves herself more!"





try:
    inp = raw_input ("Enter score between 0.0 and 1.0:")
    score = float(inp)
except:
    print 'Error, please enter a number'
    quit ()
    
if score >= 0.9 :
    print 'A'
elif score >= 0.8 :
    print 'B'
elif score >= 0.7 :
    print 'C'
elif score >= 0.6 :
    print 'D'
elif  score < 0.6 :
    print 'F'
    
    
    

