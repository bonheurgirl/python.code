#Emanuel's Code
largestso = None
smallestso = None

while True:
        num = int(raw_input("Enter a number: "))
        if inp=="done": break
        
    if smallestso is None:
        snallestso=num

    elif num < smallestso:
        smallestso=num
    
    else:
        largestso=num

print "Maximum", largestso
print "Minimum", smallestso

