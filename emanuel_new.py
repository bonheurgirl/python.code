#Emanuel's Code
largestso = None
smallestso = None

while True:
    try:
        num = int(raw_input("Enter a number: "))
        if inp=="done": break
    except:
        print "Invalid input"
        continue
    if smallestso is None:
        snallestso=num

    elif num < smallestso:
        smallestso=num
    
    else:
        largestso=num

print "Maximum", largestso
print "Minimum", smallestso

