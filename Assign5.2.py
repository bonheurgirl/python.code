"""
Exercise 5.1 Write a program which repeatedly 
reads numbers until the user enters “done”. 
Once “done” is entered, print out the total, count, 
and average of the numbers. If the user enters anything
other than a number, detect their mistake using try 
and except and print an error message and skip to the 
next number. 

Enter a number: 4  ​
 Enter a number: 5  ​
 Enter a number: bad data  ​ 
Invalid input  ​

 Enter a number: 7  
 Enter a number: done  ​
 16 3 5.33333333333”

"""

#ASSIGNMENT 5.1
count = 0
total = 0
while True:
    inp = raw_input("Enter a number: ")
    if inp == 'done' : break
    if len(inp) < 1 : break #Check for empty line, user just hits enter
    
   
    try:
        num = float(inp)
    except:
        print "Invalid input"
        continue
    count = count + 1
    total = total + num
    print num, total, count

print 'Average: ', total/count



#Excerpt From: Charles Severance. “Python for Informatics.” Michigan Publishing, 2014. iBooks. https://itun.es/us/ZZXdH.n


#5.2 Write a program that repeatedly prompts a 
#user for integer numbers until the user enters 'done'. 
#Once 'done' is entered, print out the largest and 
#smallest of the numbers. If the user enters
# anything other than a valid number catch 
#it with a try/except and put out an appropriate
# message and ignore the number. Enter the numbers 
#from the book for problem 5.1 and Match the desired 
#output as shown.

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
