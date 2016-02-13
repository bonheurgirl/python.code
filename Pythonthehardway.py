the_count = [1, 2, 3, 4, 5,]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
newlist = list()
for number in the_count:
    if number in newlist:
        continue
    if number not in newlist:
        newlist.append(number)
    print "This is count %d" % number
    print the_count
    print newlist
print the_count
print newlist


# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit
    #print fruits
print fruits

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i
    #print change
   

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)
#Adding 0 to the list.
#Adding 1 to the list.
#Adding 2 to the list.
#Adding 3 to the list.
#Adding 4 to the list.
#Adding 5 to the list.

# now we can print them out too
for i in elements:
    print "Element was: %d" % i
print elements
#Element was: 0
#Element was: 1
#Element was: 2
#Element was: 3
#Element was: 4
#Element was: 5
#[0, 1, 2, 3, 4, 5]


x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
#There are 10 types of people.
print y
#Those who know binary and those who don't.

print "I said: %r." % x
#I said: 'There are 10 types of people.'.
print "I also said: '%s'." % y
#I also said: 'Those who know binary and those who don't.'.
