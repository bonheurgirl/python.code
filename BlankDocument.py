count = 0
total = 0
while True:
    inp = raw_input("Enter a number: ")
    #DON'T PUT THE COUNT HERE!
    #handle the edge cases
    
    if inp == 'done' : break
    if len(inp) < 1 : break #Check for empty line, user just hits enter
    
    #DO THE WORK
    try:
        num = float(inp)
    except:
        print "Invalid input"
    count = count + 1
    total = total + num
    print num, total, count

print 'Average: ', total/count