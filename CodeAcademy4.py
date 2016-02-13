"""
fruit = 'banana'
print fruit[:]
print fruit[1:]
print fruit[2:]
print fruit[0:]
print fruit[-1:]
print fruit[0:1]

def piglatin():
    word = raw_input ("Write in your word in English:")
    #print word.lower()
    #print word
    newword = word[1:] + word[0:1] + 'ay'
    return newword     
print piglatin()


x = "J123"
x.isalpha()  # False

print 'Welcome to the Pig Latin Translator!'

# Start coding here!
pyg = 'ay'
original = raw_input ("Enter a word in English:")

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1:] + first + pyg
    print new_word
else:
    print 'empty'
    

zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
#the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!

zoo_animals[3]= "zebra"
print zoo_animals

letters = ['a', 'b', 'c']
letters.append('d')
print len(letters)
print letters


suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("shorts")
suitcase.append("pants")
suitcase.append("bras")

list_length = len(suitcase)# Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase


suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle =  suitcase[2:4]         # Third and fourth items (index two and three)
last   = suitcase[4:]             # The last two items (index four and five)
print first
print middle
print last

animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]              # The fourth through sixth characters
frog =  animals[6:]              # From the seventh character to the end
print cat
print dog
print frog


#USING INDEX TO FIND A STRING
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
print animals
duck_index = animals.index("duck")
print duck_index
animals.insert(duck_index, "cobra")
print animals # Observe what prints after the insert operation



my_list = [1,9,3,8,5,7]

for number in my_list:
    print number * 2

    
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

print residents['Sloth']
print residents['Burmese Python']
   

start_list = [5, 3, 1, 2, 4]
square_list = []
for num in start_list:
    print num **2
    square_list.append(num**2)
    square_list.sort()
print square_list
"""
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

menu['Eggs and Bacon'] = 3.50
menu['Hot sex on a platter'] = 100.00
menu['Hot and Spicy'] = 10.99


print "There are " + str(len(menu)) + " items on the menu."
print menu
