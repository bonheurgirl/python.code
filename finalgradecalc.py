#TO CALCULATE FINAL SCORE FOR PYTHON FOR BEGINNERS

try:
    quiz = 0

    quiz += float(raw_input ("Enter Quiz 1 results:"))
    quiz += float(raw_input ("Enter Quiz 2 results:"))
    quiz +=float(raw_input ("Enter Quiz 3 results:"))
    quiz +=float(raw_input ("Enter Quiz 4 results:"))
    quiz +=float(raw_input ("Enter Quiz 5 results:"))
    quiz +=float(raw_input ("Enter Quiz 6 results:"))
    quiz +=float(raw_input ("Enter Quiz 7 results:"))
    quiz +=float(raw_input ("Enter Quiz 8 results:"))
    quiz +=float(raw_input ("Enter Quiz 9 results:"))
    quiz +=float(raw_input ("Enter Quiz 10 results:"))
    quiz +=float(raw_input ("Enter results of Final Exam:"))
except:
    print 'Error, please enter numeric input'
    quit()
print "Quizzes and Final Exam total",quiz

try:
    assign = 0   

    assign +=float(raw_input ("Enter Hello world results (on a 1 to 10 scale):"))
    assign +=float(raw_input ("Enter Assign 2.2 results (on a 1 to 10 scale):"))
    assign +=float(raw_input ("Enter Assign 2.3 results (on a 1 to 10 scale):"))
    assign +=float(raw_input ("Enter Assign 3.1 results (on a 1 to 10 scale):"))
    assign +=float(raw_input ("Enter Assign 3.3 results (on a 1 to 10 scale):"))
    assign +=float(raw_input ("Enter Assign 4.6 results (on a 1 to 10 scale):"))
    assign +=float(raw_input ("Enter Assign 5.2 results (on a 1 to 10 scale):"))
    assign +=float(raw_input ("Enter Assign 6.5 results (on a 1 to 10 scale):"))
    assign +=float(raw_input ("Enter Assign 7.1 results (on a 1 to 10 scale):"))
    assign +=float(raw_input ("Enter Assign 7.2 results (on a 1 to 10 scale):"))
    assign +=float(raw_input ("Enter Assign 8.4 results (on a 1 to 10 scale):"))
    assign +=float(raw_input ("Enter Assign 8.5 results (on a 1 to 10 scale):"))
    assign +=float(raw_input ("Enter Assign 9.4 results (on a 1 to 10 scale):"))
    assign +=float(raw_input ("Enter Assign 10.2 results (on a 1 to 10 scale):"))
except:
    print 'Error, please enter numeric input'
    quit()
print "Assignments total",assign

try:
    extra = float(raw_input ("Enter extra-credit points? If none, please enter '0'"))
except:
    print 'Error, please enter numeric input'
    quit()
print "Extra-credit points:",extra

sum = quiz + assign + extra
print "Total points received for all quizzes, assignments, and extra-credit:",sum

if sum >= 233:
    print "You will receive a Certificate of Distinction"
elif sum >= 195:
    print "You will receive a Statement of Accomplishment"
else:
    print "Sorry....You will not receive a Statement of Accomplishment"
