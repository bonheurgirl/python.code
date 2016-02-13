largest = None
smallest = None

while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    
    if len(inp) < 1 : break
    
    try:
        num = int(inp)
    except:
        print "Invalid input"
        continue
    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num
    if num > largest:
        largest = num
   

print "Maximum", largest
print "Minimum", smallest

#Emanuel's Code
largestso = None
smallestso = None
try:
	while True:
    	num = raw_input("Enter a number: ")
    	type(num)
        #test the num var/then input through sorting
        if num > largestso:
				largestso = largest
			elif num < smallestso:
				smallestso = smallest
			else num == "done" : break
    		print num
except:
    print "Invalid input"
print "Maximum", largest
