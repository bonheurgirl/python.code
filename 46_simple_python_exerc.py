num = raw_input('Enter number:')
numb = raw_input('Enter number:')

def max(num, numb):
    if num > numb:
        return num
    else:
        return numb
print "max of 2:", max (num, numb)


num3 = raw_input('Enter number:')
def max_of_three(num, numb, num3):
    return max(max(num, numb), num3)
print "max of 3:", max_of_three (num, numb, num3)



words = ["baby"]
def string_length():
    length = 0
    for word in words:
        length +=1
        return length
print string_length()


length=0
for x in "This is a string":
    length+=1
print(length)

length=0
for x in "baby love happens when we want it to happen":
    length+=1
print(length)