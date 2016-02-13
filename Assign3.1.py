inp = raw_input("Enter Hours:")
h = float(inp)
inp= raw_input ('Enter rate:')
r = float(inp)

if h <= 40 :
    gross_pay=float(h)*float(r)
    print gross_pay
	
elif h > 40 :
	gross_pay= (40*float(r)) + (float(h)-40) * (1.5 * float(r))

print gross_pay


def hello():
    print "hello"
    return 1234

# And here is the function being used
print hello()


#this code works,,,with simplified raw input data
inp = raw_input("Enter Hours:")
hours = float(inp)
inp= raw_input ('Enter Rate:')
rate = float(inp)


if hours <=40 :
    gross_pay = hours * rate
        
else :
	gross_pay = (40*float(rate)) + (float(hours)-40) * (1.5 * float(rate))
        
print gross_pay


inp = raw_input("Enter Hours:")
h = float(inp)
inp= raw_input ('Enter rate:')
r = float(inp)

if h <=40 :
    gross_pay = h * r
        
else :
	gross_pay = (40 * r) + (h - 40) * (1.5 * r)
        
print gross_pay

#from book, this code works

inp = raw_input("Enter Hours: ")
hours = float(inp)
inp = raw_input("Enter Rate: ")
rate = float(inp)
pay = rate * hours
print "Rate", rate, "Hours", hours
print "Pay", pay



inp = raw_input("Enter Hours: ")
hours = float(inp)
inp = raw_input("Enter Rate: ")
rate = float(inp)
if hours <=40 :
    pay = rate * hours
if hours > 40 :
    pay = (40 * rate) + ((hours - 40) * (1.5 * rate))
print "Rate", rate, "Hours", hours
print "Pay", pay