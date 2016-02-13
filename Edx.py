"""
#EDx Course
#this course is using Python 3.0

#determine perimeter
height=5
width=10
area=(height * width)
perimeter=(height + width) *2
print (area)
print(perimeter)


#ask the user their age and return number of days old
age = int(input("Your age in years:"))
age1= age * 365
print ("You are", age1, "days old")

#Write a program that asks the user for an integer 'x' and prints
#the value of y after evaluating the following expression y=x2−12x+11:
x= int(input("Input any integer:"))
y= (x**2) - (12*x) + (11)
print (y)


#days of the week program
week = ['Not a valid integer', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY','FRIDAY', 'SATURDAY', 'SUNDAY']
day = int(input("Enter a positive integer between 1 and 7:"))
print(week[day])
    
#Complete the following program such that it calculates and prints the average of the elements of the given list.
sample_list = [2, 10, 3, 5]
sum=0
for num in sample_list:
    sum+=num
print(sum/len(sample_list))
"""

#ask the user their age 
age = int(input("Your age in years:"))
if age <=0:
    print ("UNBORN")
elif age > 0 and age <=150:
    print ("ALIVE")
else:
    print ("VAMPIRE")

#Write a program which asks the user to enter a positive integer 'n' (Assume that the user always enters a positive integer) and based on the following conditions
n= int(input("Input any positive integer:"))
if n % 2 ==0 and n % 3==0:
    print ("BOTH")
elif n % 2==0 or n % 3==0:
    print ("ONE")
else: 
    print ("NEITHER")
    


n= int(input("Input total number of hours worked in a week:"))
rate=8

if n <=40 :
    pay = rate * n
    
elif n > 40 and pay <=50:
    pay = (40 * rate) + ((n - 40) * (9))

else n > 50:
 pay = (40 * rate) + ((n - 40) * (10))
 
print ("YOU MADE", pay, "DOLLARS THIS WEEK")



n= int(input("Input total number of hours worked in a week:"))
rate=8

if n >168 or n < 0:
    print ("INVALID")

elif n <=40 :
    pay = rate * n
    print ("YOU MADE", pay, "DOLLARS THIS WEEK")
    
elif n >= 41 and n <=50:
    pay = (40 * rate) + ((n - 40) * (9))
    print ("YOU MADE", pay, "DOLLARS THIS WEEK")

elif n>=51 and n <=168:
    pay = (40 * rate) + ((n - 40) * (10))
    print ("YOU MADE", pay, "DOLLARS THIS WEEK")
    

n= int(input("Input total number of hours worked in a week:"))
rate=8

if n >168 or n < 0:
    print ("INVALID")

elif n <=40 :
    pay = rate * n
    print ("YOU MADE", pay, "DOLLARS THIS WEEK")
    
elif n >= 41 and n <=50:
    pay = (40 * rate) + ((n - 40) * (9))
    print ("YOU MADE", pay, "DOLLARS THIS WEEK")

elif n>=51 and n <=168:
    pay = (40 * rate) + (10 * 9) + ((n - 50) * 10)
    print ("YOU MADE", pay, "DOLLARS THIS WEEK")


n= int(input("Enter a positive integer:"))
n1= n * (
print n1
