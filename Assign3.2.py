try:
    inp = raw_input("Enter Hours:")
    hours = float(inp)
    inp= raw_input ('Enter rate:')
    rate = float(inp)
    
except:
    print 'Error, please enter numeric input'
    quit()

if hours <= 40 :
    pay = hours * rate
    print pay
	
elif hours > 40 :
	pay = (40 * rate) + (hours - 40) * (1.5 * rate)

print pay


def addtwo (a,b):
    added = a + b
    return added
    
x = addtwo (3,5)
print x