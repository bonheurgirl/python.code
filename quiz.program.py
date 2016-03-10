# -*- coding: UTF-8 -*-
from __future__ import division
import time

correct_answers = 0
incorrect_answers=150
skipped=2
total=(correct_answers+incorrect_answers) - skipped


print "The total number of questions were", total
print "Number of correct answers:", correct_answers
print "Number of wrong answers:", incorrect_answers
print "Number of Skipped Questions:", skipped
print

try:
    score = int((correct_answers/total) * 100)  
    print
    if score >= 78:
        print score,"%","score achieved" 
        print "Congratulations, You are ready to take the Google Analytics IQ Certification Exam."
    elif score >= 1:
        print score,"%","score achieved" 
        print "You may want to complete more practice questions before attempting the Google Analytics IQ Certification Exam."  
    else:
        print score,"%","score achieved" 
        print "123, you fail!"
    
except:
    print "Divide the number of correct answers by incorrect answers and multiply by 100."
    print "If your score is above 78%. Congratulations! You are ready to take the Google Analytics IQ Certification Exam."
    print "If not, you may want to complete more practice questions before attempting the Google Analytics IQ Certification Exam."  
    
print "Thank you for completing the Google Analytics Practice Program."
print "Have a nice day & good luck"
