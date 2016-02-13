#printing the current date and time
from datetime import datetime
now = datetime.now()
print now

from datetime import datetime
now = datetime.now()

current_year = now.year
current_month = now.month
current_day = now.day

from datetime import datetime
now = datetime.now()
print now

print now.year
print now.month
print now.day

print now.hour
print now.minute
print now.second

from datetime import datetime
now = datetime.now()

print '%s:%s:%s' % (now.hour, now.minute, now.second)

from datetime import datetime
now = datetime.now()

print '%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second)

def greater_less_equal_5(answer):
    if answer > 5 :
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)

def the_flying_circus(answer):
    if answer > 100 :    # Start coding here!
        return True
       
    elif answer < 100:
        return False

print the_flying_circus(answer)
        
        




























