"""
def count_small(numbers):
    total = 0
    for n in numbers:
        if n < 10:
            total = total + 1
    return total

lost = [4, 8, 15, 16, 23, 42]
small = count_small(lost)
print small

def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count = count + 1
    return count
x =["fizz","cat","fizz"]
y = fizz_count(x)
print y
    
    
prices = {"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3}
print prices

stock = {"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15}
print stock

#example
once  = {'a': 1, 'b': 2}
twice = {'a': 2, 'b': 4}
for key in once:
    print "Once: %s" % once[key]
    print "Twice: %s" % twice[key]
#Once: 1
#Twice: 2
#Once: 2
#Twice: 4
"""
 #keeping track of the produce   
prices = {"banana": 4,"apple": 2, "orange": 1.5, "pear": 3}
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}
for key in prices:
    #print key
    #print "price: %s" % prices[key]
    #print "stock: %s" % stock[key]
    print

total = 0
for key in prices:
    print key
    x = prices[key] * stock[key]
    print x
    total += prices[key] * stock[key]
print total
    