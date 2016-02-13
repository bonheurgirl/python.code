list = ["Life", "The Universe", "Everything", "Jack", "Jill", "Life", "Jill"]

# make a copy of the list. See the More on Lists chapter to explain what [:] means.
copy = list[:]
# sort the copy
copy.sort()
prev = copy[0]
del copy[0]

count = 0

# go through the list searching for a match
while count < len(copy) and copy[count] != prev:
    prev = copy[count]
    count = count + 1

# If a match was not found then count can't be < len
# since the while loop continues while count is < len
# and no match is found

if count < len(copy):
    print "First Match:", prev


bool_one = 1 > 2 and 2 < 4
print bool_one

bool_two = not 1 == 0 and 1 ==1
print bool_two
    
bool_three = (7 > 6 and not 6 > 7) or 6 > 7
print "bool_three", bool_three

bool_four = not not 0==0 and not 1 < 0
print bool_four

bool_five = (100>1000) or not 1000<1001 and 0>=0
print bool_five


# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!
print bool_one

# Make me true!
bool_two = not 1 == 0 and 1 ==1
print bool_two

# Make me false!
bool_three =  1 > 2 and 2 < 4
print "bool_three", bool_three

# Make me true!
bool_four = 3>3 or 5>4
print bool_four

# Make me true!
bool_five = (1001>1000) or not 1000<1001 and 1>=0
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
