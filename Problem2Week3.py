hours = raw_input("Enter Hours:")
rate= raw_input ('Enter rate:')
if hours <= 40 :
    gross_pay=float(hours) * float(rate)
    print gross_pay
	
elif hours > 40 :
	gross_pay=float(hours) * ((1.5)*float(rate))


print gross_pay
