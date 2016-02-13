
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] +=   50
print inventory


word='high'
letter='h'
def find(word,letter):
    index = 0
    while index < len(word):
        if word[index]== letter:
            return index
        index = index +1
    return -1
print find(word,letter)

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print count

def count(word,letter):
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    return count
print count(word,letter)

print count('hello','h')

names = ["Adam","Alex","Mariah","Martine","Columbus"]
for name in names:
    print name

# A simple dictionary
d = {"foo" : "bar"}

for key in d: 
    print d[key]  # prints "bar"
    
    
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."}

for dic in webster:
    print webster[dic]


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for number in a:
    if number % 2 ==0:
        print number
        print "We printed even number", number
 
 #functions and for loops       
def count_small(numbers):
    total = 0
    for n in numbers:
        if n < 10:
            total = total + 1
    return total

lost = [4, 8, 15, 16, 23, 42]
small = count_small(lost)
print small