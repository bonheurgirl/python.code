"""
def hello():
    print "hello"
    return 1234
# And here is the function being used
print hello()


def computepay(h,r):
        if h <= 40 :
            pay = h * r
            return pay
        elif h > 40 :
	        pay = (40 * r) + (h - 40) * (1.5 * r)
	        return pay
inp = raw_input("Enter Hours:")
h = float(inp)
inp= raw_input ('Enter rate:')
r = float(inp)
p = computepay(h,r)
print p



def hello_world():
    print "Hello World!"    
hello_world()


def hello_world():
    print "IS this supposed to be my world!"    
hello_world()

def fred():
    print "Zap"
def jane():
    print "ABC"
jane()
fred()
jane()

def hello_world():
    print "IS this supposed to be my world!"    
hello_world()

def printlyrics():
    print "this little light of mine.  i am gonna let it shine."
printlyrics()
printlyrics()
printlyrics()

#exercise 8.1 Think Python
def backwards():
    word= raw_input ("Write in your word:")
    length = len(word)
    #print length
    words = list()
    for letter in word:
        pass
        words.append(letter)
        #print letter
        #print words
    words.reverse()
    #print words
    for letter in words:
        print letter         
backwards()


def backwards():
    word= raw_input ("Write in your word:")
    words = list()
    for letter in word:
        words.append(letter)
    words.reverse()
    for letter in words:
        print letter         
backwards()

#Exercise 3.4

def do_twice(f):
    f()
    f()
    
def print_spam():
    print 'spam'
    
def do_twice(print_spam):
    print_spam()
    print_spam()
        
do_twice(print_spam)


def print_hypers():
    print 'hyped up' #this doesn't actually print anything until you call the function
    
print_hypers() #this is calling the function

"""

def f(x):
    return x*x
print "f3 function", f(3)

def f(x,y):
    z = 3
    print 'You called f(x,y) with the value x = ' + str(x) + ' and y = ' + str(y)
    print 'x * y = ' + str(x*y)
    print z   # can reach because variable z is defined in the function

f(3,2)




