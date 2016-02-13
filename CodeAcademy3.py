"""

def square(n):
    #Returns the square of a number.
    squared = n**2
    print "%d squared is %d." % (n, squared)
    return squared
    
# Call the square function on line 9! Make sure to
# include the number 10 between the parentheses.
print square(10)

def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print "%d to the power of %d is %d." % (base, exponent, result)

power(37,4)  # Add your arguments here!

#using modulus operator, %
inp = raw_input("number:")
number = int(inp)
def cube(number):
    return number*number*number
def by_three(number):
    if number % 3==0:
        return cube(number)
    else:
        return False
#print cube(number)
print by_three(number)



from math import sqrt
print sqrt (13689)

num = raw_input('Enter number:')
def distance_from_zero(num):
    if type(num) == int or type(num) == float:
        return abs(num)
    else:
        return "Nope"
print distance_from_zero(num)




num = int(float(input('Enter number:')))
def distance_from_zero(num):
    if type(num) == int or type(num) == float:
        return abs(num)
    else:
        return "Nope"
print distance_from_zero(num)

num = ('high')
def distance_from_zero(num):
    if type(num) == int or type(num) == float:
        return abs(num)
    else:
        return "Nope"
print distance_from_zero(num)



bool_one = not 3*1 < 4**1
print bool_one

bool_two = not 3**4 < 4**3
print bool_two

bool_three = not 10 % 3 <= 10 % 2
print bool_three

bool_four = not 3**2 + 4**2 != 5**2
print bool_four

bool_five = not not 11*5 < 1*5
print bool_five



bool_one = not (3*1 < 4**1) and (1>0 == 1>0)
print bool_one

bool_two = not 3**4 < 4**3
print bool_two

bool_three = not 10 % 3 <= 10 % 2
print bool_three

bool_four = not 3**2 + 4**2 != 5**2
print bool_four

bool_five = not not 11*5 < 1*5
print bool_five


def answer():
    return (42)
print answer()

def fruit_color(fruit):
    if fruit == "apple":
        return "red"
    elif fruit == "banana":
        return "yellow"
    elif fruit == "pear":
        return "green"
print fruit_color('apple')
"""

nights = int(float(input('Enter nights:')))
def hotel_cost(nights):
    return (nights*140)
print hotel_cost(nights)
city = str(raw_input('Enter city:'))
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa" :
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475
    else:
        print 'Not valid city'
        exit()
print plane_ride_cost(city)

days = int(float(input('Enter how many days you will rent the car:')))
def rental_car_cost(days):
    if days >= 7:
        return (days*40) - (50)
    elif days  >= 3:
        return (days*40) - (20)
    else:
        return (days*40)
print rental_car_cost(days)

def trip_cost(city,days):
return hotel_cost(nights) + rental_car_cost(days)+plane_ride_cost(city) +  
print trip_cost(city,days)


# Make sure that the_flying_circus() returns True
def the_flying_circus():
    if 5 >= 5 and 1 > 0 :
        return True
    elif 10==10 or 100 < 101:
        return True
    elif not 10 % 3 <= 10 % 2:
        return True
    else:
        print 'none of these'
        # You'll want to add the else statement, too!
        
print the_flying_circus()
