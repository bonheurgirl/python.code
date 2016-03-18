#Python for Kids

import random
import time

desserts = ['ice cream', 'pancakes', 'brownies', 'cookies',
'candy']

print (random.choice(desserts))



def lots_of_numbers(max):
    for x in range(0, max):
        print(x)
        
lots_of_numbers(101)



def lots_of_numbers(max):
    t1 = time.time()
    for x in range(0, max):
        print(x)
    t2 = time.time()
    t3=t2-t1
    #print('it took %s seconds' % (t2-t1))
    print "it took", t3, "seconds"
    
for x in range(1, 2):
    print(x)
    #time.sleep(1)
    print "all done"
    
    
    