"""
The break statement in Python terminates the current loop and resumes execution at the next statement, just like the traditional break found in C.

The most common use for break is when some external condition is triggered requiring a hasty exit from a loop. The break statement can be used in both while and for loops."""

for letter in 'Python':     # First Example
   if letter == 'h':
      break
   print 'BREAK STATEMENT:Current Letter :', letter
   
"""
The continue Statement:
The continue statement in Python returns the control to the beginning of the while loop. The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop.

The continue statement can be used in both while and for loops."""
   
   

for letter in 'Python':     # First Example
   if letter == 'h':
      continue
   print 'CONTINUE STATEMENT:Current Letter :', letter
   
   
"""The pass Statement:
The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.

The pass statement is a null operation; nothing happens when it executes. The pass is also useful in places where your code will eventually go, but has not been written yet (e.g., in stubs for example):
The preceding code does not execute any statement or code if the value of letter is 'h'. The pass statement is helpful when you have created a code block but it is no longer required.

You can then remove the statements inside the block but let the block remain with a pass statement so that it doesn't interfere with other parts of the code."""

 


for letter in 'Python': 
   if letter == 'h':
      pass
      print 'This is pass block'
   print 'PASS STATEMENT:Current Letter :', letter

print "Good bye!"

