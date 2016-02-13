hrs = raw_input("Enter Hours:")
h = float(hrs)
rate= raw_input ('Enter rate:')
r = float(rate)


try:
    ival = int(hrs)
except:
    ival = -1
    
if ival <= 40 :

    gross_pay=float(hrs)*float(rate)
print gross_pay

else :
    print 'Not a number'
    
try:
    ival = int(rate)
except:
    ival = -1
	
if ival > 40 :
	gross_pay= (40*float(rate)) + (float(hrs)-40) * (1.5 * float(rate))
    print gross_pay
else:
    print 'Not a number'

`