# -*- coding: UTF-8 -*-

import time


time.sleep(1)
print """Welcome to the Google Analytics Practice Exam.  
Now, it's time to get started."""

print
time.sleep(1)
print "General Knowledge Section"

print

print "gk1. Digital analytics is..."
print "a) the analysis of quantitative data from your business"
print "b) a process of continual improvement of the online experience"
print "c) the analysis of qualitative data from your business"
print "d) the analysis of data from your business and the competition"
print "e) all of these answers are correct"

correctanswers = 0
incorrectanswers=0

gk1 = raw_input("Please enter your answer: ")


if gk1 == "e" or gk1 == "E":
    print "correct!"
    correctanswers = correctanswers + 1
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1


print
print "gk2. What is the first step of analytics planning?"

print "a) Document your technical infrastructure"
print "b) Implement Google Analytics"
print "c) Create your implementation plan"
print "d) Define your overall measurement plan and business objectives"

gk2 = raw_input("Please enter your answer: ")

if gk2 == "d" or gk2 == "D":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1


print
print """gk3. Which of the following should
be the first step you complete during the
analytics planning process?

a) Implement Google Analytics
b) Create your implementation plan
c) Define your overall measurement plan and business objectives
d) Maintain and refine your plans
e) Document your technical infrastructure"""

gk3 = raw_input("Please enter your answer: ")

if gk3 == "c" or gk3 == "C":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1

print
print """gk4. It’s important to have a clear measurement strategy to
guide your implementation strategy and your data
analysis. Which of the following business objectives
would be most relevant for content publishers?

a) collecting user information for sales teams to connect with potential leads
b) selling products or services
c) encourage engagement and frequent visitation
d) all these options are equally relevant as business objectives for content publishers"""

print
gk4 = raw_input("Please enter your answer: ")

if gk4 == "c" or gk4 == "C":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1

print
print """gk5. The demographics and interest category
information in Google Analytics comes from

a) the DoubleClick third-party cookie
b) Google Tag Manager
c) survey data filled out by users
d) Information that you upload from your CRM
e) The AdWords first-party cookie"""

gk5 = raw_input("Please enter your answer: ")

if gk5 == "a" or gk5 == "A":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1

print
print """gk6.When do Google Analytics Terms of
Service permit sending personally identifying information (PII) to Google?

a) when encrypted
b) in custom campaigns only
c) never"""


gk6 = raw_input("Please enter your answer: ")

if gk6 == "c" or gk6 == "C":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
print
print """gk7. A visitor comes to your site but stops
looking at pages and generating events. Which of the
following will occur by default?

a) Google Analytics does not keep track of sessions by default
b) The visitor’s session expires after 5 minutes of inactivity
c) The visitor’s session expires once the visitor has exited your site
d) The visitor’s session expires after 30 minutes of inactivity"""


gk7 = raw_input("Please enter your answer: ")

if gk7 == "d" or gk7 == "D":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1

print
print """gk8. Which of the following would you use to set up a custom alert?

a) Intelligence
b) Real-Time
c) Conversions
d) Content"""    


gk8 = raw_input("Please enter your answer: ")

if gk8 == "d" or gk8 == "D":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1

print
print """gk9. Once your Google Analytics data has been processed, it can not be changed.

a) True
b) False"""

gk9 = raw_input("Please enter your answer: ")

if gk9 == "a" or gk9 == "A":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1


print
print """gk10. When Google Analytics processes data, one of the main tasks it completes is organizing hits into:

a) users and sessions
b) cohorts and interactions
c) registered users and browsers
d) purchasers and browsers"""

gk10 = raw_input("Please enter your answer: ")

if gk10 == "a" or gk10 == "A":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1


print
print """gk11. A session in Google Analytics consists of:

a) The reports generated by users over a specific period of time
b) Interactions or hits from a specific user for all time
c) Interactions or hits from a specific user over a defined period of time
d) A group of users getting together in person to discuss analytics"""

gk11 = raw_input("Please enter your answer: ")

if gk11 == "c" or gk11 == "C":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1

print
print """gk12. By default, an Analytics session ends when inactive for:

a) 15 minutes
b) 30 minutes
c) 45 minutes
d) 60 minutes"""

gk12 = raw_input("Please enter your answer: ")

if gk12 == "b" or gk12 == "B":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1

print """gk13. You need to immediately find out whether people
are viewing the new content that you just added today. 
Which of the following would be most useful?

a) Real-Time
b) Intelligence
c) Annotations
d) Secondary dimensions"""


print
gk13 = raw_input("Please enter your answer: ")

if gk13 == "a" or gk13 == "A":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
    
print """gk14.Which of the following would you
use to exclude rows with fewer than 10 visits?

a) table sort
b) primary dimension
c) secondary dimension
d) table filter
e) pivot table"""

print
gk14 = raw_input("Please enter your answer: ")

if gk14 == "d" or gk14 == "D":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1


print
print """gk15. In which of the following circumstances
would you want to increase the default sessions timeout
length in Google Analytics?

a) The games on your site are highly interactive.
b) A typical session on your site involves filling out at least 3 forms.
c) The default session timeout length is set dynamically by Google Analytics and you cannot change it.
d) The average length of videos on your site is 35 minutes.
e) The average article on your site takes 4 minutes to read."""


gk15 = raw_input("Please enter your answer: ")

if gk15 == "d" or gk15 == "D":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
 
print   
print """gk16.Which are the four main parts of the Google Analytics platform?

a) Configuration, Prozessing, Reporting, and Recollection
b) Configuration, Collection, Progressing, and Reporting
c) Collection, Configuration, Processing, and Reporting
d) Collection, Processing, Continuation, and Reporting"""



gk16 = raw_input("Please enter your answer: ")

if gk16 == "c" or gk16 == "C":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1

print
print """gk17.Which of the following is a session level interaction?

a) ecommerce transaction
b) All of these answers are correct.
c) social interaction
d) pageview
e) event"""

gk17 = raw_input("Please enter your answer: ")

if gk17 == "b" or gk17 == "B":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    

print   
print """gk18.Which of the following are “hit” types tracked by Google Analytics?

a) pageviews
b) events
c) all of these answers are correct
d) transactions"""


gk18 = raw_input("Please enter your answer: ")

if gk18 == "c" or gk18 == "C":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1


time.sleep(1)
print "Number of Correct Answers So far:", correctanswers

time.sleep(2)
print
print "Next Section:  Channels, Sources & Mediums"

time.sleep(1)
print
print """CSM1.Which of the following are examples of channels?.

a) Audience
b) Organic Search
c) Conversion
d) Display
e) Email
f) c, d, e
g) a, c, d, e,
h) a, b, c, d, e
i) b, d, e """

csm1 = raw_input("Please enter your answer: ")

if csm1 == "i" or csm1 == "I":
    print "correct!"
    correctanswers = correctanswers + 1
    print "Note: Other channels are Direct, Referral, Paid Search, Social."
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
print
print """CSM2.Which of the following are examples of Sources?

a) example.com
b) mail.google.com
c) All of these are possible Sources.
d) (direct)
e) google""" 

csm2 = raw_input("Please enter your answer: ")

if csm2 == "c" or csm2 == "C":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1


print
print """CSM3.Which of the following are examples of Mediums? Select all that apply.

a) Conversion
b) Example.com
c) Google
d) Email
e) All of these are Mediums."""


csm3 = raw_input("Please enter your answer: ")

if csm3 == "d" or csm3 == "D":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1

time.sleep(1)
print """Note: Other examples are Organic, CPC,
Referral, None (Direct Traffic). 
Example.com and Google are Sources."""


print
print """CSM4.Which of the following are examples of Sources? Select all that apply.

a) Email
b) Example.com
c) Search
d) Google
e) Display
f) all of the above
g) b and d"""

csm4 = raw_input("Please enter your answer: ")

if csm4 == "g" or csm4 == "G":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    

print
print"""CSM5.Which of the following is not a default Medium in Google Analytics?

a) cpc
b) referral
c) organic
d) email
e) All of these are default Mediums."""
    
csm5 = raw_input("Please enter your answer: ")

if csm5 == "d" or csm5 == "G":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
    
print
print"""CSM6.Which of the following Channels is part of the Default Channel Grouping?

a) Display
b) Direct
c) Social
d) Organic
e) All of these are part of the Default Channel Grouping."""

    
csm6 = raw_input("Please enter your answer: ")

if csm6 == "e" or csm6 == "E":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
    
print
print"""CSM7.You are interested in exploring metrics by campaign
and traffic source. Which of the following sections will havethis report information by default?

a) Behavior
b) Conversion
c) Audience
d) Admin
e) Acquisition"""

    
csm7 = raw_input("Please enter your answer: ")

if csm7 == "e" or csm7 == "E":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
   
print
print """Quick Review on Mediums: Google Analytics detects three mediums without any customization.
● The first default medium is “organic.” It represents traffic that comes from organic, or unpaid, search results.
● Another default medium is “referral.” Any traffic that comes to your site from another website that’s not a search engine will show up in your reports as a “referral.”
● The final default medium is “(none).” This medium is applied only for users that come directly to your site by either typing your URL into a browser or clicking on a bookmark. In your reports, you will see these users have a source of “direct” and a medium of “(none)."""


time.sleep(1)
print "Number of Correct Answers So far:", correctanswers

time.sleep(2)
print
print "Next Section:  Attribution Modeling"

time.sleep(1)
print """AM1.You’ve found that most of your customers
initially learned about your brand via a display ad.
Which of the following attribution models will give
credit to display ads that introduced customers to
your brand?

a) First Interaction attribution model
b) Last Non-Direct Click attribution model
c) Linear attribution model
d) Position Based attribution model
e) Last Click attribution model
f) b, c, d
g) a, c, d"""

am1 = raw_input("Please enter your answer: ")

if am1 == "g" or am1 == "G":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1


from __future__ import division
print "Number of Correct Answers:", correctanswers
print "Number of Wrong Answers:", incorrectanswers
print int((correctanswers/26) * 100),"%", "score achieved"

