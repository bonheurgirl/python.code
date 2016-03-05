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