"""nights = int(float(input('Enter nights:')))
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

spending_money = float(input('Enter how much in extras:'))
def trip_cost(city,days,spending_money):
    return plane_ride_cost(city) + days*140 + rental_car_cost(days) + spending_money
print trip_cost(city,days,spending_money)
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

spending_money = float(input('Enter how much in extras:'))
def trip_cost(city,days,spending_money):
    return plane_ride_cost(city) + days*140 + rental_car_cost(days) + spending_money
print trip_cost(city,days,spending_money)
print trip_cost("Los Angeles",5,600)
