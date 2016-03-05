#Emanuel's Code
largestso = None
smallestso = None

while True:
    num = int(raw_input("Enter a number: "))
    #test the num var/then input through sorting
    if num > largestso:
        largestso = largest
	elif num < smallestso:
	    smallestso = smallest
	else num == "done" : break
	
print num


print "Maximum", largest
print "Minimum", smallest


if smallestso is None:
    snallestso=num

elif num < smallestso:
    smallest=num
    
else num > largestso:
    largest=num
    
