#http://codingbat.com/prob/p120546
  
  
#warmup exercises  
a_smile=1
b_smile=0

def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return "TRUE"
    elif a_smile or b_smile:
        return "FALSE"
    else:
        return "TRUE"      
print monkey_trouble(a_smile, b_smile)


def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False

def sum_double(a,b):
   if a==b:
    return 2*(a + b)
   if a is not b:
    return a+b
print sum_double(1,2)
print sum_double(2,2)
    

def diff21(n):
    if n >21:
        return 2 * (n-21)
    if n <= 21:
        return 21-n
print diff21(19)
print diff21(10)
print diff21(21)