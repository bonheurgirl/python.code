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

print "Invalid input"
print "Maximum", largest
