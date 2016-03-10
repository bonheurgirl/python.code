# -*- coding: UTF-8 -*-
"""This program tests your Google Analytics Knowledge.
It is meant to be used as extra practice before you take the IQ Exam"""

from __future__ import division
import time

correct_answers = 0
incorrect_answers=0
skipped=0
total=(correct_answers+incorrect_answers) - skipped

"""Sections Covered:

1. General Knowledge
2. Channels, Sources & Mediums
3. Attribution Modeling
4. Metrics & Dimensions
5. Adwords
6. Customer Journey
7. Accounts, Views & Filters
8. Reports
9. E-commerce & Conversions
10. Segmentation
11. Events
12. Goals
13. Campaign Tracking
14. Analytics Tracking
15. Platform Principles"""



name = raw_input("Hello, what's your name?") 

time.sleep(1)
print "Hi", name
print "Welcome to the Google Analytics Exam Practice Questions."
#print "Type 's' to skip any question. Skipped questions will not affect your score."

 
time.sleep(1)
print "It's time to get started."

print
time.sleep(3)
print "General Knowledge Section"

print
time.sleep(1)
print "GK1. Digital analytics is..."
print "a) the analysis of quantitative data from your business"
print "b) a process of continual improvement of the online experience"
print "c) the analysis of qualitative data from your business"
print "d) the analysis of data from your business and the competition"
print "e) all of these answers are correct"

print
GK1 = raw_input("Please enter your answer: ")


if GK1 == "e" or GK1 == "E":
    print "correct!"
    correct_answers = correct_answers + 1

elif GK1=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1 
else:
    print "sorry, incorrect. the answer is E."
    incorrect_answers = incorrect_answers + 1


print
print "GK2. What is the first step of analytics planning?"

print "a) Document your technical infrastructure"
print "b) Implement Google Analytics"
print "c) Create your implementation plan"
print "d) Define your overall measurement plan and business objectives"

GK2 = raw_input("Please enter your answer: ")

if GK2 == "d" or GK2 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif GK2=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1
        
else:
    print "sorry, incorrect. the answer is D."
    incorrect_answers = incorrect_answers + 1


print
print """GK3. Which of the following should
be the first step you complete during the
analytics planning process?

a) Implement Google Analytics
b) Create your implementation plan
c) Define your overall measurement plan and business objectives
d) Maintain and refine your plans
e) Document your technical infrastructure"""

GK3 = raw_input("Please enter your answer: ")

if GK3 == "c" or GK3 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
elif GK3=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1         
else:
    print "sorry, incorrect. the answer is C."
    incorrect_answers = incorrect_answers + 1

print
print "GK4. It’s important to have a clear measurement strategy to"
print "guide your implementation strategy and your data"
print "analysis. Which of the following business objectives"
print "would be most relevant for content publishers?"

print "a) collecting user information for sales teams to connect with potential leads"
print "b) selling products or services"
print "c) encourage engagement and frequent visitation"
print "d) all these options are equally relevant as business objectives for content publishers"

print
GK4 = raw_input("Please enter your answer: ")

if GK4 == "c" or GK4 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
elif GK4=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1         
else:
    print "sorry, incorrect. the answer is C."
    incorrect_answers = incorrect_answers + 1

print
print """GK5. The demographics and interest category
information in Google Analytics comes from

a) the DoubleClick third-party cookie
b) Google Tag Manager
c) survey data filled out by users
d) Information that you upload from your CRM
e) The AdWords first-party cookie"""

GK5 = raw_input("Please enter your answer: ")

if GK5 == "a" or GK5 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
elif GK5=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1      
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1

print
print "GK6. When do Google Analytics Terms of"
print "Service permit sending personally identifying information (PII) to Google?"

print "a) when encrypted"
print "b) in custom campaigns only"
print "c) never"


GK6 = raw_input("Please enter your answer: ")

if GK6 == "c" or GK6 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
elif GK6=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1           
else:
    print "sorry, incorrect. the answer is C."
    incorrect_answers = incorrect_answers + 1
    
print
print """GK7. A visitor comes to your site but stops
looking at pages and generating events. Which of the
following will occur by default?

a) Google Analytics does not keep track of sessions by default
b) The visitor’s session expires after 5 minutes of inactivity
c) The visitor’s session expires once the visitor has exited your site
d) The visitor’s session expires after 30 minutes of inactivity"""


GK7 = raw_input("Please enter your answer: ")

if GK7 == "d" or GK7 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
elif GK7=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1             
else:
    print "sorry, incorrect. the answer is D."
    incorrect_answers = incorrect_answers + 1

print
print """GK8. Which of the following would you use to set up a custom alert?

a) Intelligence
b) Real-Time
c) Conversions
d) Content"""    


GK8 = raw_input("Please enter your answer: ")

if GK8 == "a" or GK8 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
elif GK8=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1             
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1

print
print """GK9. Once your Google Analytics data has been processed, it can not be changed.

a) True
b) False"""

GK9 = raw_input("Please enter your answer: ")

if GK9 == "a" or GK9 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
elif GK9=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1            
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1


print
print "K10. When Google Analytics processes data, one of the main tasks"
print "it completes is organizing hits into:"

print "a) users and sessions"
print "b) cohorts and interactions"
print "c) registered users and browsers"
print "d) purchasers and browsers"

GK10 = raw_input("Please enter your answer: ")

if GK10 == "a" or GK10 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
elif GK10=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1               
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1


print
print """GK11. A session in Google Analytics consists of:

a) The reports generated by users over a specific period of time
b) Interactions or hits from a specific user for all time
c) Interactions or hits from a specific user over a defined period of time
d) A group of users getting together in person to discuss analytics"""

GK11 = raw_input("Please enter your answer: ")

if GK11 == "c" or GK11 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
elif GK11=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1                
else:
    print "sorry, incorrect. the correct answer is C."
    incorrect_answers = incorrect_answers + 1

print
print """GK12. By default, an Analytics session ends when inactive for:

a) 15 minutes
b) 30 minutes
c) 45 minutes
d) 60 minutes"""

GK12 = raw_input("Please enter your answer: ")

if GK12 == "b" or GK12 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
elif GK12=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1                
else:
    print "sorry, incorrect. the correct answer is B."
    incorrect_answers = incorrect_answers + 1

print """GK13. You need to immediately find out whether people
are viewing the new content that you just added today. 
Which of the following would be most useful?

a) Real-Time
b) Intelligence
c) Annotations
d) Secondary dimensions"""


print
GK13 = raw_input("Please enter your answer: ")

if GK13 == "a" or GK13 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
elif GK13=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1                
else:
    print "sorry, incorrect. the correct answer is A."
    incorrect_answers = incorrect_answers + 1
    
    
print """GK14.Which of the following would you
use to exclude rows with fewer than 10 visits?

a) table sort
b) primary dimension
c) secondary dimension
d) table filter
e) pivot table"""

print
GK14 = raw_input("Please enter your answer: ")

if GK14 == "d" or GK14 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
elif GK14=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1                
else:
    print "sorry, incorrect. the correct answer is D."
    incorrect_answers = incorrect_answers + 1


print
print """GK15. In which of the following circumstances
would you want to increase the default sessions timeout
length in Google Analytics?

a) The games on your site are highly interactive.
b) A typical session on your site involves filling out at least 3 forms.
c) The default session timeout length is set dynamically by
Google Analytics and you cannot change it.
d) The average length of videos on your site is 35 minutes.
e) The average article on your site takes 4 minutes to read."""


GK15 = raw_input("Please enter your answer: ")

if GK15 == "d" or GK15 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
elif GK15=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1                
else:
    print "sorry, incorrect. the correct answer is D."
    incorrect_answers = incorrect_answers + 1
 
print   
print """GK16.Which are the four main parts of the Google Analytics platform?

a) Configuration, Processing, Reporting, and Recollection
b) Configuration, Collection, Progressing, and Reporting
c) Collection, Configuration, Processing, and Reporting
d) Collection, Processing, Continuation, and Reporting"""



GK16 = raw_input("Please enter your answer: ")

if GK16 == "c" or GK16 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
elif GK16=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1                
else:
    print "sorry, incorrect. the correct answer is C."
    incorrect_answers = incorrect_answers + 1

print
print """GK17.Which of the following is a session level interaction?

a) ecommerce transaction
b) All of these answers are correct.
c) social interaction
d) pageview
e) event"""

GK17 = raw_input("Please enter your answer: ")

if GK17 == "b" or GK17 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
elif GK17=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1                
else:
    print "sorry, incorrect. the correct answer is B) All these are session level interactions"
    incorrect_answers = incorrect_answers + 1
    

print   
print """GK18.Which of the following are “hit” types tracked by Google Analytics?

a) pageviews
b) events
c) all of these answers are correct
d) transactions"""


GK18 = raw_input("Please enter your answer: ")

if GK18 == "c" or GK18 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
elif GK18=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1                
else:
    print "sorry, incorrect. the answer is C) All of them are hits tracked by GA."
    incorrect_answers = incorrect_answers + 1


time.sleep(1)
print "Number of correct answers so far:", correct_answers
print "Number of incorrect answers so far:", incorrect_answers

time.sleep(2)
print
print "Next Section:  2. Channels, Sources & Mediums"

time.sleep(1)
print
print """CSM1. Which of the following are examples of channels?.

a) Audience
b) Organic Search
c) Conversion
d) Display
e) Email
f) c, d, e
g) a, c, d, e
h) a through e
i) b, d, e """

csm1 = raw_input("Please enter your answer: ")

if csm1 == "i" or csm1 == "I":
    print "correct!"
    correct_answers = correct_answers + 1
    print "Note: Other channels are Direct, Referral, Paid Search, Social."
elif csm1=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1              
else:
    print "sorry, incorrect. the answer is I) Organic Search, Display, & Email."
    incorrect_answers = incorrect_answers + 1
    time.sleep(2)  
    #definition of Channel
    print "Channel is a group of several traffic sources from the same medium."
    print "Channels are in the Acquisition Reports."
    time.sleep(1)  


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
    correct_answers = correct_answers + 1
elif csm2=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1          
else:
    print "sorry, incorrect. the answer is C) All of these are possible Sources."
    incorrect_answers = incorrect_answers + 1
    time.sleep(2)  
    #definition of Source
    print "Traffic source dimensions. Every referral to a web site has an origin, or source. Possible sources include: “google” (the name of a search engine), “facebook.com” (the name of a referring site), “spring_newsletter” (the name of one of your newsletters), and “direct” (users that typed your URL directly into their browser, or who had bookmarked your site)"
    time.sleep(1)

print
print """CSM3. Which of the following are examples of Mediums? Select all that apply.

a) Conversion
b) Example.com
c) Google
d) Email
e) All of these are Mediums."""


csm3 = raw_input("Please enter your answer: ")

if csm3 == "d" or csm3 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
elif csm3=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1  
else:
    print "sorry, incorrect. the answer is D."
    incorrect_answers = incorrect_answers + 1

time.sleep(1)
print """Note: Other examples are Organic, CPC,
Referral, None (Direct Traffic). 
Example.com and Google are Sources."""

time.sleep(1)
print
print """CSM4. Which of the following are examples of Sources? Select all that apply.

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
    correct_answers = correct_answers + 1
elif csm4=="s":
    print "GO TO THE NEXT QUESTION."      
else:
    print "sorry, incorrect. the answer is G) Example.com and Google."
    incorrect_answers = incorrect_answers + 1
    

print
print"""CSM5.Which of the following is not a default Medium in Google Analytics?

a) cpc
b) referral
c) organic
d) email
e) All of these are default Mediums."""
    
csm5 = raw_input("Please enter your answer: ")

if csm5 == "d" or csm5 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
elif csm5=="s":
    print "GO TO THE NEXT QUESTION."        
else:
    print "sorry, incorrect. the answer is d) email is not a default medium."
    incorrect_answers = incorrect_answers + 1
    
    
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
    correct_answers = correct_answers + 1
elif csm6=="s":
    print "GO TO THE NEXT QUESTION."          
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""CSM7. You are interested in exploring metrics by campaign
and traffic source. Which of the following sections will have this report information by default?

a) Behavior
b) Conversion
c) Audience
d) Admin
e) Acquisition"""

    
csm7 = raw_input("Please enter your answer: ")

if csm7 == "e" or csm7 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
elif csm7=="s":
    print "GO TO THE NEXT QUESTION."          
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
   
print
print "Quick Review on Mediums: Google Analytics detects three mediums without any customization."
time.sleep(1)
print "The first default medium is “organic.” It represents traffic that comes from organic, or unpaid, search results."
time.sleep(1)
#print "Another default medium is “referral.” Any traffic that comes to your site from another website that’s not a search engine will show up in your reports as a “referral.”
time.sleep(1)
print "The final default medium is “(none).” This medium is applied only for users that come directly to your site by either typing your URL into a browser or clicking on a bookmark. In your reports, you will see these users have a source of “direct” and a medium of “(none)."
#End of Section

time.sleep(1)
print "Number of Correct Answers So far:", correct_answers
print "Number of Incorrect Answers So far:", incorrect_answers

time.sleep(2)
print
print "Next Section:  3. Attribution Modeling"

time.sleep(1)
print """AM1. You’ve found that most of your customers
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
    correct_answers = correct_answers + 1
elif am1=="s":
    print "GO TO THE NEXT QUESTION."           
else:
    print "sorry, incorrect. the answer is G)First Interaction attribution model"
    print "Linear attribution model &  Position Based attribution model"
    incorrect_answers = incorrect_answers + 1

print
print"""AM2.Channel X has an Assisted/Last Interaction Conversion
value of exactly 1. Which of the following is true?

a) Channel X equally initiates and assists conversions
b) Channel X always initiates conversions
c) Channel X is always the last click before conversion
d) None of these is true"""


am2 = raw_input("Please enter your answer: ")

if am2 == "d" or am2 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
elif am2=="s":
    print "GO TO THE NEXT QUESTION."            
else:
    print "sorry, incorrect. the answer is D. "
    incorrect_answers = incorrect_answers + 1
    
print """Note: The correct answer would be Channel X
equally assists and completes conversions."""


print
print"""AM3.In the Linear attribution model...

a) each touchpoint in the conversion path share
equal credit for the conversion

b) the last touchpoint receives 100% of the 
credit for the conversion

c) the touchpoints closest in time to the 
conversion get most of the credit

d) the first touchpoint receives 100% credit
for the conversion"""

am3 = raw_input("Please enter your answer: ")

if am3 == "a" or am3 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
elif ame=="s":
    print "GO TO THE NEXT QUESTION."              
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""AM4.Which of the following most accurately
describes the concept of attribution in digital
analytics?

a) calculating cost per click
b) determining a user’s device
c) calculating ROI
d) assigning credit for conversions
e) determining a traffic source"""


am4 = raw_input("Please enter your answer: ")

if am4 == "d" or am4 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
elif am4=="s":
    print "GO TO THE NEXT QUESTION."              
else:
    print "sorry, incorrect. the answer is D."
    incorrect_answers = incorrect_answers + 1

print
print"""AM5.Which of the following attribution
models would be useful for evaluating ads and
campaigns that are designed to create initial
awareness about a brand?

a) Last Interaction model
b) Last Non-Direct Click model
c) Linear model
d) First Interaction model"""

am5 = raw_input("Please enter your answer: ")

if am5 == "d" or am5 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
elif am5=="s":
    print "GO TO THE NEXT QUESTION."              
else:
    print "sorry, incorrect. the answer is D."
    incorrect_answers = incorrect_answers + 1

print
print"""AM6.A customer visits your site four
times in a month before making a $100 purchase
on your site. She first comes to your site by
clicking on a search ad, then a social media ad,
then another search ad, and finally a display ad.
If you’re using a linear attribution model, how 
much conversion credit could be assigned to the
last display ad?

a) $0
b) $25
c) $50
d) $100"""

am6 = raw_input("Please enter your answer: ")

if am6 == "b" or am6 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
elif am6=="s":
    print "GO TO THE NEXT QUESTION."              
else:
    print "sorry, incorrect. the answer is B."
    print "Note: The conversion credit is calculated"
    print "as follows: purchase value/touch-points in the"
    print "conversion path = 100/4 = 25"
    incorrect_answers = incorrect_answers + 1
print


print
print"""AM7. Direct is the traffic source when no other
traffic source is available (e. g. bookmark or directly typed in
browswer)

a) true
b) false
""" 
am7 = raw_input("Please enter your answer: ")

if am7 == "a" or am7 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
elif am7=="s":
    print "GO TO THE NEXT QUESTION."           
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1
    
 #check question   
print
print"""AM8.  In the case of a "direct" visit, where visitor
has a previous source, the previous source gets credit for
visit.

a) true
b) false"""

am8 = raw_input("Please enter your answer: ")

if am8 == "b" or am8 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
elif am8=="s":
    print "GO TO THE NEXT QUESTION."           
else:
    print "sorry, incorrect.  the answer is B."
    incorrect_answers = incorrect_answers + 1
#end of Attribution Modeling Section



print
print
time.sleep(1)
print "Number of correct answers So far:", correct_answers
print "Number of incorrect answers So far:", incorrect_answers
time.sleep(2)
print
print "Next Section: 4.  Metrics & Dimensions"

time.sleep(1)
print """MD1. Which of the following suggests a poorly performing landing page?
a) Bounce Rate > 90%
b) Bounce Rate < 90%
c) % New Visits > 90%
d) % New Visits < 90%
e) None of these answers"""

md1 = raw_input("Please enter your answer: ")

if md1 == "a" or md1 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
elif md1=="s":
    print "GO TO THE NEXT QUESTION."           
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1
    
    
    
print
print"""MD2. Which of the following Behavior metrics
shows the number of sessions that included a view of a page?

a) Visits
b) Unique Pageviews
c) Pageviews
d) Bounce rate
e) Unique Visits"""

md2 = raw_input("Please enter your answer: ")

if md2 == "a" or md2 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
elif md2=="s":
    print "GO TO THE NEXT QUESTION."           
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1

#start here
print
print"""MD3.Which of the following are valid scopes for dimensions?

a) user level, campaign level, session level, hit level
b) campaign level, session level, hit level
c) session level, hit level
d) none of these answers is correct
e) user level, session level, hit level"""

md3 = raw_input("Please enter your answer: ")

if md3 == "e" or md3 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is E."
    incorrect_answers = incorrect_answers + 1

print
print"""MD4. You want to explore traffic metrics by
gender and age. Which of the following sections in
Analytics will be most useful?

a) Behavior
b) Conversion
c) Admin
d) Audience
e) Acquisition"""


md4 = raw_input("Please enter your answer: ")

if md4 == "d" or md4 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1

print
print"""MD5.Which of the following are measures of traffic volume?

a) Avg. Time on Site
b) Margin
c) Bounce Rate
d) Visits"""


md5 = raw_input("Please enter your answer: ")

if md5 == "d" or md5 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""MD6.Which of the following reporting
dimensions would be useful to reference if
you were rebuilding a website?

a) Browser
b) Device category
c) Language
d) All of these dimensions
e) None of these dimensions"""

md6 = raw_input("Please enter your answer: ")

if md4 == "d" or md4 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1

print """Note: There also exists a version of this
question where “device category” is replaced by
“screen colors”. The answer is of course the same."""


print
print"""MD7.Which of the following metrics shows the
number of times your ads were displayed?

a) Impressions
b) CTR
c) Visits
d) Clicks
e) Pageviews"""

md7 = raw_input("Please enter your answer: ")

if md7 == "a" or md7 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
print
print"""MD8.Which of the following are dimensions?

a) % New Sessions
b) Bounce rate
c) Conversion Rate
d) Screen resolution
e) Region
f) d, e
g) a, d"""

md8 = raw_input("Please enter your answer: ")

if md8 == "f" or md8 == "F":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1

print
print"""MD9.Which of the following are dimensions?

a) Conversion Rate
b) % New Sessions
c) Bounce Rate
d) Region"""
    
md9 = raw_input("Please enter your answer: ")

if md9 == "d" or md9 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""MD10. The following are examples of dimensions:

(select all that apply)

a) Traffic source
b) Page name
c) Country
d) Unique visitors
e) a, b, c
f) a, b, c, d
"""

md10 = raw_input("Please enter your answer: ")

if md10 == "e" or md10 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is E."
    incorrect_answers = incorrect_answers + 1


print
print"""MD11.Your business objective is to maximize
the number of sales through your website. Which of
the following metrics would most directly help you
measure performance against this objective?

a) Ecommerce Conversion Rate
b) Bounce Rate
c) Pages/Visit
d) Visits
e) Page Value"""

md11 = raw_input("Please enter your answer: ")

if md11 == "a" or md11 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""MD12.You want to see conversion rates
for Windows visits coming from London. Which
of the following dimensions would you need to select?

a) City, and Goal Conversion Rate as a secondary dimension

b) Operating System, and City as a secondary dimension

c) Goal Conversion Rate, and City as a secondary dimension

d) any one of these options"""



md12 = raw_input("Please enter your answer: ")

if md12 == "b" or md12 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""MD13.Which of the following reporting
tools would you use to show the dimension “city”
next to the dimension “source” in a report?

a) Date comparison
b) Table filter
c) Table sort
d) Plot rows
e) Primary dimension
f) Secondary dimension
g) Pie chart
h) Pivot table"""
    
md13 = raw_input("Please enter your answer: ")

if md13 == "f" or md13 == "F":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
 
print
print"""MD14. Which of the following metrics would
be most useful in measuring how many conversions were
initiated by Paid Search?

a) Assisted Conversion Value
b) First Interaction (Click) Conversions
c) Conversion Rate
d) None of these metrics"""
   
md14 = raw_input("Please enter your answer: ")

if md14 == "b" or md14 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is B."
    incorrect_answers = incorrect_answers + 1


print
print"""MD15. Which of the following are metrics?

a) City
b) % New Visits
c) Pageviews
d) Browser
e) b, c"""

md15 = raw_input("Please enter your answer: ")

if md15 == "e" or md15 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
print
print"""MD16. The following are examples of metrics:

a) Unique visitors
b) Page name
c) Average visit duration
d) Traffic source
e) a, c
f) b, d"""
   
md16 = raw_input("Please enter your answer: ")

if md16 == "e" or md16 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
print
print"""MD17. Which of the following would be
most useful for optimizing landing pages?

a) Unique Visits
b) Unique Pageviews
c) Visits
d) Pageviews
e) Bounce Rate"""
    
md17 = raw_input("Please enter your answer: ")

if md17 == "e" or md17 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""MD18. Which two metrics below would be the
best KPIs for measuring the performance of an ecommerce
business?

a) bounce rate and average session duration
b) pageviews and revenue
c) pageviews and bounce rate
d) revenue and average order value"""

md18 = raw_input("Please enter your answer: ")

if md18 == "d" or md18 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
   
print
print"""MD19. Every metric may be combined with every
dimension in Google Analytics.

a) True
b) False"""
 
md19 = raw_input("Please enter your answer: ")

if md19 == "b" or md19 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""MD20. You can combine a metric X with a
dimension Y in Google Analytics

a) as long as sampling is not required

b) if X and Y have been precalculated together in an aggregate table

c) if X and Y are in the same channel grouping

d) if X and Y have the same campaign

e) if X and Y have the same scope"""
    
md20 = raw_input("Please enter your answer: ")

if md20 == "e" or md20 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
print """Explanation: Not every metric can be combined
with every dimension. Each dimension and metric has a
scope: users, sessions, or actions. It only makes sense
to combine dimensions and metrics that share the same scope.
For example, Sessions is a session-based metric so it can only
be used with session-level dimensions like Source or City. It
would not be logical to combine Sessions with an action-level
(or, hit-level) dimension like Page."""
    

print
print"""MD21.  You want to create a report comparing
the performance of pages on your site and decide to use
the following dimensions and metrics: Page Title,
Avg. Visit Duration, Goal 1 Conversion Rate. Which of
the following statements is true about this report?

a) Google Analytics will allow you to create this report,
and the report makes sense since you chose to combine
hit-level metrics with the hit-level dimension Page Title.

b) Google Analytics will allow you to create this report,
but the report does not make sense since you chose to combine
session-level metrics with the hit-level dimension Page Title.

c) Google Analytics will not allow you to create this report."""

md21 = raw_input("Please enter your answer: ")

if md21 == "b" or md21 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
#End of Metrics & Dimensions Section    


print
time.sleep(1)
print "Number of Correct Answers So far:", correct_answers

time.sleep(2)
print
print "Next Section:  5. Google AdWords"

time.sleep(1)
print
print """AW1. Which of the following AdWords reports
would you use to investigate when you should
modify your bidding during certain hours of
the day to optimize conversions?

a) AdWords Keywords
b) Hour of Day
c) Destination URLs
d) Placements
e) Campaigns"""


AW1 = raw_input("Please enter your answer: ")

if AW1 == "b" or AW1 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1

print
print """AW2. If a paid keyword has an Assisted/Last Click
or Direct Conversion value of .5, which of the following is true?

a) The keyword played an assist role in exactly one conversion
b) The keyword played an assist role in exactly five conversions
c) The keyword played an assist role less often than it played a last click role
d) none of these answers"""

AW2 = raw_input("Please enter your answer: ")

if AW2 == "c" or AW2 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1

print"""Note: In this example the value is 0.5. That means for example
5 assists and 10 last click or direct conversions = 5/10 = 0,5. If the
value would be about 1, the paid keyword played equally an assisted and
completed role. If the value would be greater than 1, the keyword
played an assisted role."""

print
print"""AW3. You want to evaluate the landing pages
you are using for AdWords ads. Which of the following
dimensions would be most useful?

a) Destination URL
b) Ad Group
c) Campaign
d) Placements
e) Keyword"""

AW3 = raw_input("Please enter your answer: ")

if AW3 == "a" or AW3 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""AW4. Which of the following AdWords reports
would you use to investigate whether you should
modify your bidding during certain hours of the
day to optimize conversions?

a) Campaigns
b) Keywords
c) Search Queries
d) Time of Day
e) Destination URLs"""

   
AW4 = raw_input("Please enter your answer: ")

if AW4 == "d" or AW4 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""AW5. Which of the following would help you to
determine the conversion value of a paid keyword?

a) Multi-Channel Funnels
b) CPM
c) CTR
d) Real-Time
e) none of these answers"""

   
AW5 = raw_input("Please enter your answer: ")

if AW5 == "a" or AW5 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    

print
print"""AW6. Which of the following metrics would allow you
to assess AdWords campaign profitability?

a) Revenue per Click
b) CTR
c) ROI
d) Margin
e) CPM"""  
  
AW6 = raw_input("Please enter your answer: ")

if AW6 == "c" or AW6 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1



print
print"""AW7. Which of the following are possible ways to
view the dimension “Ad Content” in your Google Analytics
AdWords reports?

Check all that apply.

a) Switch the primary dimension in the AdWords Campaigns report to “Ad Content”
b) Switch the primary dimension in the AdWords Keywords report to “Ad Content”
c) Add “Ad Content” to the Campaigns report as a secondary dimension
d) all the above
e) b, c
f) a, c"""
    
AW7 = raw_input("Please enter your answer: ")

if AW7 == "e" or AW7 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
print
print"""AW8. Which of the following Google Analytics dimensions
are only available for AdWords traffic?

Check all that apply.

a) Medium
b) Matched Search Query
c) Query Match Type
d) Placement Domain
e) Source
f) Campaign
g) all the above
h) b, c, d
i) a, d, e"""

AW8 = raw_input("Please enter your answer: ")

if AW8 == "h" or AW8 == "H":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
 
print
print"""AW9.  Adwords has a 30 day window for conversion.
 
 a) true
 b) false
 c) there is no window for conversion
""" 
 
AW9 = raw_input("Please enter your answer: ")

if AW9 == "a" or AW9 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""AW10.  AdWords shows the conversion on the date of conversion.

a) true
b) false
c) AdWords does not show conversion rates.
"""

AW10 = raw_input("Please enter your answer: ")

if AW10 == "b" or AW10 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1

time.sleep(2)  
print """AdWords shows the conversion on the date the ad was displayed.
Google Analytics on the date of conversion."""
#end of Google Adwords Section   

print
time.sleep(1)
print "Number of Correct Answers So far:", correct_answers

time.sleep(2)
print
print "Next Section:  6. Customer Journey"

time.sleep(1)
print
print"""CJ1. Which of the following would be most useful in
measuring how many days passed between the first visit
to a site and the eventual conversion?

a) Time Lag
b) Conversion Value
c) Path Length
d) Top Conversion Paths
e) Assisted/Last Interaction Conversions"""


CJ1 = raw_input("Please enter your answer: ")

if CJ1 == "a" or CJ1 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
elif CJ1=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1         
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1

print
print"""CJ2. Your Multi-Channel Funnel reports have no
data. What is the most likely reason?

a) You haven’t implemented Goals or Ecommerce
b) Your are not using Content Experiments
c) You haven’t enabled demographic data
d) You haven’t set up Goal Funnels
e) You are not using Google Tag Manager"""

CJ2 = raw_input("Please enter your answer: ")

if CJ2 == "a" or CJ2 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
elif CJ2=="s":
    print "GO TO THE NEXT QUESTION."
    skipped = skipped + 1        
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1

print
print"""CJ3. You’ve noticed that many users visit your site several
times before converting and you want to understand in more detail
how they arrive at your site. Which of the following metrics would
be most helpful in showing you whether a keyword is part of a conversion
path?

a) Visits
b) Assisted Conversions
c) Bounce Rate
d) Impressions
e) Clicks"""
   
CJ3 = raw_input("Please enter your answer: ")

if CJ3 == "b" or CJ3 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
print
print"""CJ4. What is Bounce Rate?

a) the percentage of visits when a visitor viewed
only one page and then exited without a second interaction on the site

b) the percentage of times unique visitors returned
to your website in a given time period

c) the percentage of sessions for which a visitor
exits from your homepage

d) the percentage of site exits"""


CJ4 = raw_input("Please enter your answer: ")

if CJ4 == "a" or CJ4 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1



print
print"""CJ5. Why might a site have a high Bounce Rate?

a) The landing page of the site has extra Event Tracking
implemented to track additional actions besides pageviews.

b) The ads that bring the users to the site set different
expectations than the landing page.

c) The site only has one page (e.g. a simple blog).

d) The page that your users typically land on doesn’t
have enough information or a good call-to-action.

e) all the above

f) b, c, d

g) a, c, d"""


CJ5 = raw_input("Please enter your answer: ")

if CJ5 == "f" or CJ5 == "F":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""CJ6.   True or False. In order to see data in the
Multi-Channel Funnels reports you must first implement Goals or Ecommerce.

a) True
b) False"""

CJ6 = raw_input("Please enter your answer: ")

if CJ6 == "a" or CJ6 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""CJ7. Which of the following Multi-Channel
Funnels reports would you use to see the most
common sequences of marketing touch points that
lead to conversions on your site or app?

a) Assisted Conversions
b) Top Conversion Paths
c) Time Lag
d) Path Length"""

CJ7 = raw_input("Please enter your answer: ")

if CJ7 == "b" or CJ7 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    

print
print"""CJ8. Google Analytics can recognize returning users

a) on websites only
b) on websites, Android mobile apps
c) on websites, iOS mobile apps, Android mobile apps
d) Google Analytics cannot recognize returning users on any device."""


CJ8 = raw_input("Please enter your answer: ")

if CJ8 == "c" or CJ8 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
#end of Customer Journey Section

print
time.sleep(1)
print "Number of Correct Answers So far:", correct_answers

time.sleep(2)
print
print "Next Section:  7. Accounts, Views & Filters"

time.sleep(1)

print
print"""AVF1. True or False: The order in which filters appear
in your view settings matters.

a) True. Filters are executed in the order in which they appear.

b) False. Filters are not necessarily executed in the order in
which they appear."""

AVF1 = raw_input("Please enter your answer: ")

if AVF1 == "a" or AVF1 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1

print
print"""AVF2. Which of the following are possible uses of filters?

a) replace complicated page URLs with readable text strings
b) report on only a subdomain or directory
c) include only traffic coming from a particular campaign
d) exclude visits from a particular IP address
e) all of these are possible uses of filters"""


AVF2 = raw_input("Please enter your answer: ")

if AVF2 == "e" or AVF2 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
print
print"""AVF3. Why is it important that you maintain
one unfiltered view when using filters with your Analytics account?

a) You will need to configure your goals in the unfiltered view

b) Without one unfiltered view, you will not be able to use a
filter for multiple views

c) An unfiltered view ensures that the original data an always be accessed

d) There is no reason to maintain an unfiltered view"""

AVF3 = raw_input("Please enter your answer: ")

if AVF3 == "c" or AVF3 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1



print
print"""AVF4. Your company has a website and a mobile app,
and you want to track each separately in Google Analytics.
How should you structure your account(s)?

a) One account, one property, no views
b) One account, two properties
c) One account, one property, two views
d) One account, one property, one view, because
you can’t use Google Analytics to track the mobile app"""


AVF4 = raw_input("Please enter your answer: ")

if AVF4 == "b" or AVF4 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""AVF5. Which of the following are possible
uses of views within a single Google Analytics account?

a) To look more closely at traffic to a specific part
of a site (a page or selection of pages)

b) To limit a user’s access to a subset of data

c) To track domains that belong to another account

d) To look more closely at traffic to a specific subdomain

e) all the above

f) a, b, d

g) a, b, c"""

AVF5 = raw_input("Please enter your answer: ")

if AVF5 == "f" or AVF5 == "F":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""AVF6.  You want a second view of your data where you
only see traffic to a specific subdirectory. What is the best
way to set this up?

a) Create a new view and apply an advanced filter that
deletes page data outside the subdirectory

b) Create a duplicate view and add a filter: select
“Include only traffic to a subdirectory” from the Filter
Type drop down, and specify the subdirectory

c) Create a second Google Analytics account, and apply
the new tracking code to the pages in the subdirectory

d) Create a new web property and add the new tracking
code to the pages on the subdirectory"""

AVF6 = raw_input("Please enter your answer: ")

if AVF6 == "b" or AVF6 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1

print
print"""AVF7.  Using filters, you can _______.

a) exclude data from a view
b) change how the data looks in your reports
c) include data in a view
d) All of these answers apply"""

AVF7 = raw_input("Please enter your answer: ")

if AVF7 == "d" or AVF7 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
  
print
print"""AVF8. Which of the following best represents the hierarchical
structure of a Google Analytics account from top to bottom?

a) View → Account → Property
b) Property → Account → View
c) Account → View → Property
d) Account → Property → View"""

AVF8 = raw_input("Please enter your answer: ")

if AVF8 == "d" or AVF8 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
print
print """AVF9. Which of the following statements are true?


a) If you make a mistake with a configuration
setting on a view, you can always reprocess the data to fix it.

b) To view data from two websites in aggregate using
Google Analytics, you must use the same tracking ID
on both sites.


c) Once a view is deleted it can be restored using
the trash can feature.

d) When a new view is created, it will show the
historical data from the first view you created for the property

e) all the above

f) b, c, d

g) b, c"""

AVF9 = raw_input("Please enter your answer: ")

if AVF9 == "g" or AVF9 == "G":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
print
print"""AVF10.  Filters can modify the data in
your Google Analytics reports by:


a) including data
b) excluding data
c) exporting data
d) changing how data looks in reports
e) all the above
f) a, b, d
g) b, d
"""

AVF10 = raw_input("Please enter your answer: ")

if AVF10 == "f" or AVF10 == "F":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
#end of Accounts, Views, & Filters    

print
time.sleep(1)
print "Number of correct answers so far:", correct_answers

time.sleep(2)
print
print "Next Section: 8. Reports"
time.sleep(1)


print
print"""R1.  Which of the following would you use to
show two date ranges on the same graph?

a) secondary dimension
b) motion chart
c) plot rows
d) pivot table
e) date comparison"""


R1 = raw_input("Please enter your answer: ")

if R1 == "e" or R1 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""R2. Which of the following reporting tools
would you use to show two rows of data on the same graph?

a) Date comparison
b) Table filter
c) Table sort
d) Plot rows
e) Primary dimension
f) Secondary dimension
g) Pie chart
h) Pivot table"""


R2 = raw_input("Please enter your answer: ")

if R2 == "d" or R2 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
print
print"""R3. Which of the following Audience reports
would you use to see how often users return to your site?

a) Location reports
b) Language
c) Frequency & Recency reports
d) New vs. Returning reports
e) Engagement reports
f) Browser & OS reports
g) Mobile reports"""

R3 = raw_input("Please enter your answer: ")

if R3 == "c" or R3 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    

    
print
print"""R4. The URL for the homepage of your site is example.com/index.
You would like this to appear as “/home” in your Pages report.
How can this be achieved?

a) Use a Search and Replace custom filter on the Request
URI field where Search Strings is “/index” and Replace String is “/home”

b) Use a Search and Replace custom filter on the Request URI field
where Search String is “www.example.com/index” and Replace String
is “www.example.com/home”
"""
R4 = raw_input("Please enter your answer: ")

if R4 == "a" or R4 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""R5. Which of the following would be most
useful for ranking pages according to revenue contribution?

a) Page Value
b) Bounce Rate
c) Revenue
d) ROI
e) Margin"""

R5 = raw_input("Please enter your answer: ")

if R5 == "a" or R5 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""R6. To see the bounce rate of a specific medium in an
Acquisitions report:

a) Change the primary dimension in the Channels report to
“Medium” and view the Bounce Rate metric

b) Change the primary dimension in the Source/Medium
report to “Medium” and view the Bounce Rate metric

c) Change the primary dimension in the Referrals report
to “Medium” and view the Bounce Rate metric

d) You cannot see this information in any Acquisitions reports.

e) All the above

f) a, b

g) a, c, d
"""
R6 = raw_input("Please enter your answer: ")

if R6 == "f" or R6 == "F":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""R7. Which of the following types of traffic will
show in the “Campaigns” report?

a) Visits from Google AdWords campaigns that have autotagging enabled

b) Visits from Google AdWords campaigns that have autotagging disabled
and no manual campaign tagging

c) Visits from all links tagged with the parameter utm_medium=cpc

d) Visits from all links tagged with the utm_campaign parameter

e) all the above

f) a, b, c

g) a, d

h) b, c, d

"""

R7 = raw_input("Please enter your answer: ")

if R7 == "g" or R7 == "G":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
    
    
print
print"""R8. Which of the following reports allows
you to identify the terms visitors use to conduct
searches within your site?

a) Keyword report
b) Affinity Categories
c) Search Engine Optimization report
d) Site Search report"""


R8 = raw_input("Please enter your answer: ")

if R8 == "d" or R8 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1




print
print"""R9.  The Site Search reports show:

a) how users search your site
b) traffic coming from search engines
c) traffic coming from Google organic search
d) traffic coming from Google paid search"""

R9 = raw_input("Please enter your answer: ")

if R9 == "a" or R9 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1




print
print"""R10.  Which of the following Audience reports would you use to see how your site performance differs between desktop, smartphone and tablet users?

a) Location reports
b) Language
c) Frequency & Recency reports
d) New vs. Returning reports
e) Engagement reports
f) Browser & OS reports
g) Mobile reports"""

R10 = raw_input("Please enter your answer: ")

if R10 == "g" or R10 == "G":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""R11. You are interested in identifying the most popular
content on your site. Which of the following sections will
have this report information by default?

a) Search
b) Acquisition
c) Audience
d) Conversion
e) Behavior"""


R11 = raw_input("Please enter your answer: ")

if R11 == "e" or R11 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""R12. True or False: When you share a link to a custom report,
you share the data in the report.

a) True: Sharing a link to a custom report shares the data in the report.
b) False: Sharing a link to a custom report only shares a template for
the report."""

R12 = raw_input("Please enter your answer: ")

if R12 == "b" or R12 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1



print
print """R13.  Which of the following types of data can be
collected and reported in the Site Speed reports?

a) button click response time
b) how quickly images load
c) All of these are tracked by the Site Speed reports.
d) page-load time for a sample of pageviews on your site
e) how quickly the browser parses a page and makes it
available for user interaction"""

R13 = raw_input("Please enter your answer: ")

if R13 == "c" or R13 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""R14. Which of the following reporting tools
would you use to exclude any rows of a report with fewer than 50 visits?

a) Date comparison
b) Table filter
c) Table sort
d) Plot rows
e) Primary dimension
f) Secondary dimension
g) Pie chart
h) Pivot table"""

R14 = raw_input("Please enter your answer: ")

if R14 == "b" or R14 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    

print
print"""R15.  Which of the following techniques would you use
to exclude rows with fewer than 10 visits from a report table?

a) add a primary dimension
b) sort the table by sessions from highest to lowest
c) use a pivot table with two dimensions
d) add a secondary dimension
e) apply a table filter"""

R15 = raw_input("Please enter your answer: ")

if R15 == "e" or R15 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1  


print
print"""R16. Which of the following Audience reports would you use to determine whether first-time site visitors or repeat site visitors spend more time on your site on average?

a) Location reports
b) Language
c) Frequency & Recency reports
d) New vs. Returning reports
e) Engagement reports
f) Browser & OS reports
g) Mobile reports"""


R16 = raw_input("Please enter your answer: ")

if R16 == "d" or R16 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1

print
print"""R17. True or False. It is possible to customize the default
channels in the Channels report and create your own custom channels
from scratch.

a) True
b) False"""

R17 = raw_input("Please enter your answer: ")

if R17 == "a" or R17 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1



print
print"""R18. Which of the following Behavior reports would you use to identify the pages of your site that have the highest bounce rate as the first page of a user’s session?

a) All Pages
b) Content Drilldown
c) Landing Pages
d) Exit Pages
e) Site Speed
f) Site Search
g) Events"""

R18 = raw_input("Please enter your answer: ")

if R18 == "c" or R18 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""Which of the following Behavior reports could you use to find new keyword ideas for your search advertising campaigns?

a) All Pages
b) Content Drilldown
c) Landing Pages
d) Exit Pages
e) Site Speed
f) Site Search
g) Events"""

R19 = raw_input("Please enter your answer: ")

if R19 == "f" or R19 == "F":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""R20.  Which of the following are required to create a Custom Report?


a) A report title must be entered
b) Multiple report tabs must be created
c) Multiple metric groups must be created
d) At least one metric must be added
e) At least one dimension must be added
f) A report filter must be applied
g) All the above
h) a, b, c
i) a, d, e
j) c, f, g
"""
R20 = raw_input("Please enter your answer: ")

if R20 == "i" or R20 == "I":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1



print
print"""R21. True or False. Custom Reports will only
display data for the date range selected at the time the report is created.

a) True
b) False

"""

R21 = raw_input("Please enter your answer: ")

if R21 == "b" or R20 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""R22. You can retrieve Google Analytics
reporting data through the following methods:


a) the account administration settings
b) the reporting interface
c) the SDKs
d) an API
e) All the above
f) a, b
g) b, d
h) c, d
"""
R22 = raw_input("Please enter your answer: ")

if R22 == "c" or R22 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    

print
print """R23. The reporting APIs can be used to:


a) automate complex reporting tasks
b) automate your tracking code customizations
c) retrieve Google Analytics data for use in your own applications
d) build your own dashboard with Google Analytics data
e) a, b, c,
f) all the above
g) a c, d
h) c, d
"""   
R23 = raw_input("Please enter your answer: ")

if R23 == "g" or R23 == "G":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""R24. Each query sent to the Reporting API must specify:


a) the start and end dates
b) the name of the standard report you wish to use
c) which metrics to display
d) the ID of the account view that the data should be retrieved from
e) all the above
f) a, b, c
g) a, c, d
"""
R24 = raw_input("Please enter your answer: ")

if R24 == "g" or R24 == "G":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""R25.  If the data for a report you request is stored in a standard aggregate table, it will never be sampled in Google Analytics.

a) True
b) False"""

R24 = raw_input("Please enter your answer: ")

if R24 == "a" or R24 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""R26.  If you decrease the sample size for a report, 
more sessions will be used to calculate the report and it
will take longer to generate.

a) True
b) False"""

R26 = raw_input("Please enter your answer: ")

if R26 == "b" or R26 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""R27.You can adjust the sample size by:

a) adding a segment to your report
b) adjusting the session timeout control
c) adjusting a control in the reporting interface
d) specifying the sample size when querying the API
e) all the above
f) a, b, c
g) c, d,
h) b, c, d
"""

R27 = raw_input("Please enter your answer: ")

if R27 == "g" or R27 == "G":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
#end of Reports Section


print
time.sleep(1)
print "Number of Correct Answers So far:", correct_answers

time.sleep(2)
print
print "Next Section:  9. E-commerce & Conversions"



print
print"""EC1.  eCommerce & Conversions
Your ecommerce site sells colorful wrist watches that visitors
can customize using a tool online. Which of the following represent(s)
a micro conversion for your site?

a) an offline sale
b) an online sale
c) a view of the home page
d) All of these are mirco conversions for this site.
e) Use of the “customize your watch” tool"""


EC1 = raw_input("Please enter your answer: ")

if EC1 == "e" or EC1 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1



print
print"""EC2.  Which of the following represents a macro
conversion for an ecommerce site?

a) receiving a product inquiry
b) a completed sales transaction
c) collecting a lead
d) a click on a “buy” button
e) all of the above"""

EC2 = raw_input("Please enter your answer: ")

if EC2 == "b" or EC2 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""EC3.  You run a heavy-machinery business and use
your website to generate sales leads for high-priced items.
Which of the following actions below would you consider the
main “macro conversion” for your site?

a) A potential customer visits a lead form, but doesn’t fill it out or submit it.
b) A potential customer fills out and submits a lead form.
c) A potential customer downloads a spec sheet for one of your machines.
d) A potential customer signs up for your weekly newsletter.
e) A potential customer joins your social media community."""

EC3 = raw_input("Please enter your answer: ")

if EC3 == "b" or EC3 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""EC4.  A macro conversion

a) Occurs when someone completes an action that’s important to your business
b) Is your highest converting campaign
c) Always occurs prior to a micro conversion
d) Is a large revenue sale that is directly attributable to a display campaign
e) Occurs when over 50% of visitors buy an item"""

EC4 = raw_input("Please enter your answer: ")

if EC4 == "a" or EC4 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""EC5.  Person A and person B each visits
your commerce site once. During her visit, person
A buys one of your products. Then, before leaving
the site, she makes another purchase. Person B buys
nothing. What is your ecommerce conversion rate for
these two visits?

a) 0%
b) 100%
c) 50%
d) 33%
e) 200%"""



EC5 = raw_input("Please enter your answer: ")

if EC5 == "b" or EC5 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1

print
print"""Note: The ecommerce conversion rate is calculated
like this: number of transactions / visits = 2/2 = 1 = 100%"""


print
print"""EC6. You want to know whenever weekly revenue for your
“spring sale” campaign increases or decreases by 10%.
Which of the following would me most useful?

a) Secondary Dimensions
b) Intelligence Alerts
c) Annotations
d) Real-Time"""

EC6 = raw_input("Please enter your answer: ")

if EC6 == "b" or EC6 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""EC7.  Which of the following is true of ROI?

a) If Cost is $5 and Revenue is $5, your ROI is 50%
b) If Cost is $5 and Revenue is $5, your ROI is 100%
c) If Cost is $5 and Revenue is $5, your ROI is 0%
d) If Cost is $5 and Revenue is $5, your ROI is 20%
e) None of these answers are true of ROI"""

EC7 = raw_input("Please enter your answer: ")

if EC7 == "c" or EC7 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    print
    
print"""Note: ROI is calculated like this: revenue minus cost / cost = (5 – 5)/5 = 0/5 = 0"""

print
print"""EC8. To calculate ROI correctly, Google Analytics
needs

a) Cost
b) Operating Cost
c) Margin
d) Interest Rate
e) Revenue
f) All the above
g) a, b, e
h) a, e
i) d, e
"""
EC8 = raw_input("Please enter your answer: ")

if EC8 == "h" or EC8 == "H":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""EC9.  Which of the following should you NOT
collect with the Google Analytics ecommerce JavaScript?

a) tax amount
b) credit card number
c) billing city
d) purchase amount
e) product SKU(s)"""

EC9 = raw_input("Please enter your answer: ")

if EC9 == "b" or EC9 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""EC10. In order to set up ecommerce tracking, you need to_________.

a) have linked an AdWords account with your Google Analytics account

b) enable ecommerce tracking in at least one of the views for a property

c) add ecommerce tracking JavaScript to your receipt page or
“transaction complete” page

d) add an ecommerce campaign variable to your URLs

e) all the above

f) none of the above

g) a, c, d

h) b, c

i) b, c, d
"""

EC10 = raw_input("Please enter your answer: ")

if EC10 == "h" or EC10 == "H":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the correct answer is H"
    incorrect_answers = incorrect_answers + 1


print
print"""EC11.  Which of the following questions could
you answer with the Ecommerce reports?

a) Which product category brings in the most revenue for my business?
b) What are the ten most frequently purchased products on my site?
c) What products did a visitor purchase together in the same transaction?
d) What is the average order value of the transactions placed on my site?
e) All the above.
f) None of the above.
g) a, b, c
h) b, c, d
i) a, d
j) c, d

"""
EC11 = raw_input("Please enter your answer: ")

if EC11 == "e" or EC11 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is e) all the above."
    incorrect_answers = incorrect_answers + 1
    
print
print"""EC12.  You must place ecommerce tracking code after standard tracking code.

a) true
b) false
"""
EC12 = raw_input("Please enter your answer: ")

if EC12 == "a" or EC12 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1  
#end of E-Commerce & Conversions Section

print
time.sleep(1)
print "Number of Correct Answers So far:", correct_answers

time.sleep(2)
print
print "Next Section:  10. Segmentation"
time.sleep(1)



print
print"""S1.  Which of the following would be valid segments to
consider when looking at data? Select all that apply.

a) traffic by device
b) traffic by geography
c) traffic by marketing channel
d) traffic by time of day
e) all of the above"""


S1 = raw_input("Please enter your answer: ")

if S1 == "e" or S1 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1  
    
    

print
print"""S2.  Which of the following would be valid segments
to consider using to analyze traffic patterns in your data?

a) All of these answers are correct.
b) traffic by time of day
c) traffic by device category
d) traffic by marketing channel
e) traffic by geography"""


S2 = raw_input("Please enter your answer: ")

if S2 == "a" or S2 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1  


print
print"""S3.  Which of the following are true about segmentation?

a) Segmentation can help you find the underlying causes of changes to your aggregate data.
b) Segmentation allows you to isolate and analyze subsets of your data.
c) Segmentation should generally not be used without Real-Time reporting.
d) Segmentation is a technique that should only be used by experienced analysts.
e) All of the above.
f) a, b, c
g) a, b
"""
S3 = raw_input("Please enter your answer: ")

if S3 == "g" or S3 == "G":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1  


print
print"""S4. Which of the following are true about segmentation?

a) Segmentation allows you to combine data from multiple web properties in your reports.
b) Segmentation allows you to isolate and analyze subsets of your data.
c) Segmentation is a technique that should only be used by experienced analysts.
d) Segmentation can help you find the underlying causes of changes to your aggregate data.
e) All of the above.
f) b, d
g) c, d
h) a, b, c

"""
S4 = raw_input("Please enter your answer: ")

if S4 == "f" or S4 == "F":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1  
    
    
print
print"""S5. Segments can be created using dimensions or metrics.

a) true
b) false"""

S5 = raw_input("Please enter your answer: ")

if S5 == "a" or S5 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1   
#End of Segmentation Section

print
time.sleep(1)
print "Number of Correct Answers So far:", correct_answers

time.sleep(2)
print
print "Next Section:  11. Events"
time.sleep(1)


print
print"""E1.  You want to know whether button X is clicked more often than button Y.
Which of the following would be most useful?

a) Events
b) Annotations
c) Intelligence
d) Real-Time"""

E1 = raw_input("Please enter your answer: ")

if E1 == "a" or E1 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1  


print
print"""E2.  You want to measure the percentage of sessions
during which the user clicks a “product detail” button.
Which of the following would you need to do in order to see this information?

a) Track the button as a page view and look at the Events Overview
b) Track the button with an event and set up an event goal
c) Enable the button as a KPI and set up a dashboard
d) Set up a “product details” button in the ecommerce JavaScript
e) None of these options will work"""


E2 = raw_input("Please enter your answer: ")

if E2 == "b" or E2 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1 



print
print"""E3.  You want to see the percentage of sessions in which a
specific button was clicked. Which of the following would be most useful?

a) set up Real-Time reporting
b) set up a dashboard
c) set up an event goal
d) set up a custom report"""


E3 = raw_input("Please enter your answer: ")

if E3 == "c" or E3 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""E4.  In order to see data in the Events reports,
which of the following must you do in addition to implementing
the standard Google Analytics tracking code on your site?

a) Set up Event Tracking on the Account settings page and
specify which types of events you want to track

b) Set up Event Tracking on the Property settings page
and specify which types of events you want to track

c) Add additional Event Tracking code to each action on your
site that you want Google Analytics to track as an event

d) None of the above. Events are automatically tracked
with the standard Google Analytics tracking code."""

E4 = raw_input("Please enter your answer: ")

if E4 == "c" or E4 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    

print
print"""E5. Virtual pageviews track activity that doesn't generate a pageview.  

a) true
b) false"""

E5 = raw_input("Please enter your answer: ")

if E4 == "a" or E4 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1

print    
time.sleep(3)
print """What is usually meant by a “virtual pageview” is a
pageview that requires some additional tagging effort
(is not part of the main/template GA code). You need to use
them everywhere where content is loaded without a reload of
the page or when two or more pieces of content can reside on
the same URL (because of form submits)."""
#End of Events Section

print
time.sleep(5)
print "Number of Correct Answers So far:", correct_answers

time.sleep(2)
print
print "Next Section: 12. Goals"
time.sleep(3)


print
print"""G1. Which of the following could be measured by defining a goal in Google Analytics?

a) The percentage of visits that contain only one page view
b) The percentage of visits during which visitors spent at least two minutes on the site
c) The percentage of visits that result in a site registration
d) Conversion rate
e) All of these could be measured by defining a goal in Google Analytics"""

G1 = raw_input("Please enter your answer: ")

if G1 == "e" or G1 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1


print
print"""G2.Which of the following could be measured by
defining a goal in Google Analytics? Check all that apply.

a) The percentage of sessions that result in a site registration
b) The percentage of sessions that are unique
c) The percentage of sessions which contain three or more pageviews
d) The percentage of sessions during which users spend at least 2 minutes on the site
e) All the above
f) None of the above
g) a, c, d
h) a, b, c
"""
G2 = raw_input("Please enter your answer: ")

if G2== "g" or G2 == "G":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    


print
print"""G3. When configuring a goal, why is it useful to assign a goal value?

a) To determine the conversion rate
b) To calculate ecommerce metrics
c) To determine the popularity of each of your pages
d) To attribute monetary value to non-ecommerce conversions
"""
    
G3 = raw_input("Please enter your answer: ")

if G3 == "d" or G3 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
 
 
 
 
print
print"""G4. Which of the following questions can be answered using the goal flow report?

a) Is there a place in my funnel where traffic loops back to the beginning of the conversion process to start over?
b) Are there a lot of unexpected exits from a step in the middle of my conversion funnel?
c) Are there any steps in my conversion process that don’t perform well on mobile devices compared to desktop devices?
d) Do visitors usually start my conversion process from the first step or somewhere in the middle?
e) All of these can be answered using the goal flow report."""
   
G4 = raw_input("Please enter your answer: ")

if G4 == "e" or G4 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    

print
print"""G5. You have defined goal X such that any PDF download qualifies
as a goal conversion. A user comes to your site once and downloads five
PDFs. How many goal conversions will be recorded?

a) 2
b) 0
c) 5
d) 1"""


G5 = raw_input("Please enter your answer: ")

if G5 == "d" or G5 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1

time.sleep(3)
print
print"""This is probably the question that most people get wrong. The answer is indeed 1,
not 5 goal conversions.

Here is an explanation: There is an important difference between Goal conversions
and ecommerce transactions. A Goal conversion can only be
counted once during a visit, but an ecommerce transaction
can be counted multiple times during a visit. Let’s say that
you set one of your Goals to be a PDF download and you define
it such that any PDF download is a valid Goal conversion. And
let’s also say that the Goal is worth $5. In this case, if a user
comes to your site and downloads five PDF files during a single
session, you’ll only get one conversion worth $5. However, if
you were to track each of these downloads as a $5 ecommerce transaction,
you would see five transactions and $25 in ecommerce revenue."""


print
time.sleep(5)


print
print"""G6. Setting up goals allows you to see________.

a) bounce rate
b) conversion rates
c) a list of transactions
d) ecommerce revenue"""

 
G6 = raw_input("Please enter your answer: ")

if G6== "b" or G6 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
print
print"""G7. Your web property is “www.example.com”. 
You set up a URL goal of “/thankyou” and a Match
Type of “Begins with”. Which of the following
URLs will count as goals?

a) www.example.com/thankyou.html
b) www.example.com/thankyou/receipt.php
c) All of these would count as goals.
d) www.example.com/thankyou.php  """ 
    
G7 = raw_input("Please enter your answer: ")

if G7 == "c" or G7 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect."
    incorrect_answers = incorrect_answers + 1
    
time.sleep(3)
print
print"""G8. Create a goal in the “Master Profile” for the website
to match the following pages:

www.mysite.com/thankyou/shoes
www.mysite.com/thankyou/shirt
www.mysite.com/thankyou

What match type and URI pattern did you use to create the goal in your account?

a) Match type: Equals to; URI pattern: /thankyou
b) Match type: Begins with; URI pattern: /thankyou
c) Match type: Equals to; URI pattern: www.mysite.com/thankyou
d) Match type: Begins with; URI pattern: www.mysite.com/thankyou """

  
G8 = raw_input("Please enter your answer: ")

if G8 == "b" or G8 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is B."
    incorrect_answers = incorrect_answers + 1

print
print
print"""G9.Specifying a goal value allows Google Analytics to calculate __________.

a) Revenue per Click
b) Bounce Rate
c) Average Order Value
d) Ecommerce Revenue
e) Goal Revenue    
"""
G9 = raw_input("Please enter your answer: ")

if G9 == "e" or G9 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is E."
    incorrect_answers = incorrect_answers + 1


print
print
print"""G10. When configuring a goal, why is it useful to assign a goal value?

a) To attribute monetary value to a non e-commerce site
b) To calculate e-commerce metrics
c) To determine the popularity of webpages
d) You must assign a goal value in order to track conversions   
"""
G10 = raw_input("Please enter your answer: ")

if G10 == "a" or G10 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1
    
    
print
print
print"""G11. Which of the following would prevent URL destination
goal conversions from being recorded?

a) There was a misspelling in the URL of the goal definition
b) The tracking code is missing from the conversion page
c) The match type in the goal definition is incorrect
d) No URL destination goals have been defined
e) All of these answers apply   
"""
G11 = raw_input("Please enter your answer: ")

if G11 == "e" or G11 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is E."
    incorrect_answers = incorrect_answers + 1
    
    
print
print
print"""G12. Which of these best defines a Destination goal in Google Analytics?

a) A website page viewed by the user once they have completed a desired action
b) A KPI
c) A page that has given you revenue
d) The most popular page on your site   
"""
G12 = raw_input("Please enter your answer: ")

if G12 == "a" or G12 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1
    
    
print
print
print"""G13.  You define a Destination goal by:

a) Adding the e-commerce code to the goal page
b) Adding the conversion ID to the tracking code on the goal page
c) Dragging the goal page onto a Standard Report
d) Specifying the conversion page in your view settings within Google Analytics  
"""
G13 = raw_input("Please enter your answer: ")

if G13 == "d" or G13 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is D."
    incorrect_answers = incorrect_answers + 1
    
    
print
print
print"""G14.   Which of the following are required in order to
see data for each page of a three-page conversion process in
the Goal Flow report?

a) You must have Ecommerce reporting implemented.
b) You must set up a Goal for the conversion.
c) You must set up each of the three pages as a funnel step in the Goal settings.
d) None of the above. Goal Flow reports are automatically populated with data about
your conversion processes.
e) All the above
f) a, b, c,
g) a, c
h) b, c
"""
G14 = raw_input("Please enter your answer: ")

if G14 == "h" or G14 == "H":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is H."
    incorrect_answers = incorrect_answers + 1
    
    
print
print
print"""G15. Google Analytics Goals let you specify:

a) which users are likely to convert
b) which interactions should be used to calculate conversions
c) which users spend the most time on your home page
d) which page or screen is the first of a user’s visit    
"""
G15 = raw_input("Please enter your answer: ")

if G15 == "b" or G15 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is B."
    incorrect_answers = incorrect_answers + 1
#end of Goals Section

    
print
print
time.sleep(1)
print "Number of Correct Answers So far:", correct_answers

time.sleep(2)
print
print "Next Section: 13. Campaign Tracking"
time.sleep(1)



print
print"""CT1. Which of the following is NOT a standard Google Analytics campaign variable?

a) utm_adgroup
b) utm_source
c) utm_term
d) utm_content
"""
CT1 = raw_input("Please enter your answer: ")

if CT1 == "a" or CT1 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1


print
print"""CT2. Which of the following is a valid tagged custom campaign?

a) www.example.com?utm_medium=email&utm_source=newsletter1&utm_campaign=spring
b) www.example.com?utm_medium=referral&utm_source=example&utm_campaign=winter
c) www.example.com?utm_medium=cpc&utm_source=mysearch&utm_campaign=spring&utm_term=backpacks
d) www.example.com?utm_campaign=fall&utm_medium=email&utm_source=newsletter1&utm_content=a1
e) they are all valid tagged custom campaigns
"""
CT2 = raw_input("Please enter your answer: ")

if CT2 == "e" or CT2 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is E."
    incorrect_answers = incorrect_answers + 1


print
print"""CT3. What is the purpose of the URL builder?

a) to generate a URL with tracking parameters
b) to optimize landing pages
c) using the URL builder is required in order to track AdWords visits
d) to generate the URL tracking parameters that need to be appended to an organic search result
"""
CT3 = raw_input("Please enter your answer: ")

if CT3 == "a" or CT3 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1

   
print
print"""CT4.  Which is the recommended parameter for identifying different versions of an ad?

a) utm_ad
b) utm_medium
c) utm_creative
d) utm_content
"""
CT4 = raw_input("Please enter your answer: ")

if CT4 == "d" or CT4 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is D."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""CT5.   For each user who comes to your site, Google Analytics
automatically captures which of the following Traffic Source dimensions?

a) Source and Medium
b) Source, Medium, Campaign, and Ad Content
c) Campaign and Medium
d) Campaign and Ad Content
"""
CT5 = raw_input("Please enter your answer: ")

if CT5 == "a" or CT5 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""CT6.  Which of the following traffic mediums are automatically tracked by
Google Analytics without extra tagging or account linking?

a) search
b) referral
c) cpc
d) organic
e) email
f) display
g) ppc
h) all the above
i) (none), when the traffic source is “direct”
j) b, d, f
k) b, d, i

"""
CT6 = raw_input("Please enter your answer: ")

if CT6 == "k" or CT6 == "K":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is K."
    incorrect_answers = incorrect_answers + 1
    
print
print"""CT7. Which campaign tracking variables should you always use when manually tagging a URL?

a) utm_content, utm_campaign
b) utm_source, utm_medium, utm_campaign
c) utm_source, utm_content
d) utm_campaign, utm_adgroup, utm_term
"""
CT7 = raw_input("Please enter your answer: ")

if CT7 == "b" or CT7 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is B."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""CT8. Which of the following should you manually tag
with campaign tracking variables?

a) Banner ads
b) AdWords campaigns
c) Referrals
d) Organic search traffic
e) Non-AdWords CPC campaigns
f) Email campaigns
g) All the above
h) None of the above
i) a, e, f
j) a, c, d, e

"""
CT8 = raw_input("Please enter your answer: ")

if CT8 == "i" or CT8 == "I":
    print "correct!"
    correct_answers = correct_answers + 1
        
else:
    print "sorry, incorrect. the answer is I."
    incorrect_answers = incorrect_answers + 1
# end of Campaign Tracking Section   

print
print
print
time.sleep(3)
print "Number of Correct Answers So far:", correct_answers

time.sleep(2)
print
print "Next Section:  14. Analytics Tracking Code"
time.sleep(1)


print
print"""AT1.  You should add Analytics tracking code to your site___________________

a) before documenting your business objectives
b) after implementation planning
c) when it’s convenient for your IT team
d) during measurement planning
"""
AT1 = raw_input("Please enter your answer: ")

if AT1 == "b" or AT1 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif AT1=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is B."
    incorrect_answers = incorrect_answers + 1


print
print"""AT2. You should include Google Analytics tracking code on every page of a website you want to track.

a) True
b) False
"""
AT2 = raw_input("Please enter your answer: ")

if AT2 == "a" or AT2 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif AT2=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1


print
print"""AT3.  Which of the following would most
quickly allow you to determine whether the Google
Analytics code snippet is working on a specific website page?

a) Annotations
b) Real-Time
c) Secondary dimensions
d) Intelligence Alerts
"""
AT3 = raw_input("Please enter your answer: ")

if AT3 == "b" or AT3 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif AT3=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is B."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""AT4.  True or False: To collect mobile application data with
Google Analytics, you should implement the exact same code you use
for your website tracking.
a) true
b) false

"""
AT4 = raw_input("Please enter your answer: ")

if AT4 == "b" or AT4 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif AT4=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is B."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""AT5.  Which of the following technologies on
your site influence how you implement Analytics?

a) Server redirects
b) Query string parameters
c) Flash and AJAX events
d) Responsive web design
e) all of these answers are correct
"""
AT5 = raw_input("Please enter your answer: ")

if AT5 == "e" or AT5 == "E":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif AT5=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is E."
    incorrect_answers = incorrect_answers + 1
    
    
    
print
print"""AT6. The code snippet for tracking websites
with Google Analytics is written in:

a) AJAX
b) Flash
c) JavaScript
d) PHP
"""
AT6 = raw_input("Please enter your answer: ")

if AT6 == "c" or AT6 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif AT6=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is C."
    incorrect_answers = incorrect_answers + 1
    
    
    
print
print"""AT7.  Which of the following platforms is
Google Analytics capable of tracking?

a) User activity on a website
b) User activity on a mobile website
c) User activity on a mobile application
d) User activity on a gaming console
e) User activity on any digitally connected device
f) All the above
"""
AT7 = raw_input("Please enter your answer: ")

if AT7 == "f" or AT7 == "F":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif AT7=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is F."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""AT8. Which of the following would you use
to send data from a website to Google Analytics?

a) Campaign Tracking paramenter
b) JavaScript tracking code
c) none of these would be appropriate
d) Google Analytics mobile SDK
"""
AT8 = raw_input("Please enter your answer: ")

if AT8 == "b" or AT8 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif AT8=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is B."
    incorrect_answers = incorrect_answers + 1
    
    
    
print
print"""AT9.  Which of the following would you use to send data
from a web connected point-of-sale system to Google Analytics?

a) Measurement Protocol
b) any of these would be appropriate
c) Campaign Tracking parameter
d) JavaScript tracking code
e) Google Analytics mobile SDK
"""
AT9 = raw_input("Please enter your answer: ")

if AT9 == "a" or AT9 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif AT9=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1
    
    
    
print
print"""AT210.  It is recommended that you place the
Google Analytics javascript tracking code:

a) just after the opening <head> tag
b) just before the closing </head> tag
c) just after the opening <footer> tag
d) just before the closing </footer> tag
"""
AT10 = raw_input("Please enter your answer: ")

if AT10 == "b" or AT10 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif AT10=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is B."
    incorrect_answers = incorrect_answers + 1
    
    
    
print
print"""AT11.  The tracking code in Google Analytics:

a) connects data to your specific Google Analytics account
b) sends data back to your Google Analytics account for reporting
c) tracks changes in your AdWords account
d) identifies new and returning users
e) all the above
f) a, b, d
g) a, b, c
"""
AT11 = raw_input("Please enter your answer: ")

if AT11 == "f" or AT11 == "F":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif AT11=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is F."
    incorrect_answers = incorrect_answers + 1
    
    
    
print
print"""AT12.  The same type of Google Analytics tracking
code should be used for both a website and a mobile app.

a) True
b) False
"""
AT12 = raw_input("Please enter your answer: ")

if AT12 == "b" or AT12 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif AT12=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is B."
    incorrect_answers = incorrect_answers + 1
    
    
    
print
print"""AT13.Press s to go to next question....
"""
AT13 = raw_input("Please enter your answer: ")

if AT13 == "b" or AT13 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif AT13=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is ."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""AT14.  In order to distinguish between users on web pages,
Google Analytics:

a) uses the IP address of a device that accesses the site
b) uses the city, state and country of a visitor that access the site
c) creates anonymous unique identifiers using third-party cookies
d) creates anonymous unique identifiers using first-party cookies
"""
AT14 = raw_input("Please enter your answer: ")

if AT14 == "d" or AT14 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif AT14=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is D."
    incorrect_answers = incorrect_answers + 1
    
    
print
print"""AT15.  Third-party data may be joined
with the Google Analytics data collected via the tracking code.

a) True
b) False
"""
AT15 = raw_input("Please enter your answer: ")

if AT15 == "a" or AT15 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif AT15=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1



    
print
print"""AT16.  How is Google Analytics able to determine if a group
of website interactions are all from the same user device?

a) By detecting what city, operating system and browser the hits come from
b) By setting a unique ID for the device that is attached to each hit
c) By grouping together all hits that are collected within a 30 minute time period
d) Google Analytics is not able to detect if a group of interactions are from the same user device
"""
AT16 = raw_input("Please enter your answer: ")

if AT16 == "b" or AT16 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif AT16=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is B."
    incorrect_answers = incorrect_answers + 1



    
print
print"""AT17.  Rather than using the random numbers
that the tracking code creates, you can override the
unique ID with your own number.

a) True
b) False
"""
AT17 = raw_input("Please enter your answer: ")

if AT17 == "a" or AT17 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif AT17=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1
#End of Analytics Tracking Section


print
print
print
time.sleep(3)
print "Number of Correct Answers So far:", correct_answers
print "Number of Incorrect Answers So far:", incorrect_answers

time.sleep(2)
print
print "Next Section:  15. Platform Principles"
time.sleep(1)


#1.2 Platform Fundamentals
print
print"""PP1.  During data Processing, Google Analytics:

a) transforms the raw data from Collection using the Configuration settings
b) collects the data from Analytics tracking code added to a website, mobile application or other digital environment
c) lets you access and analyze your data using the Reporting interface
d) lets you adjust Configuration settings before data is collected
"""
PP1 = raw_input("Please enter your answer: ")

if PP1 == "a" or PP1 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif PP1=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1

print
print"""PP2.  Google Analytics is able to measure if a user is a first time visitor or repeat visitor.
a) True
b) False

"""
PP2 = raw_input("Please enter your answer: ")

if PP2 == "a" or PP2 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif PP2=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1

#1.3 The Data Model
print
print"""PP3.  What is the hierarchy of the Google Analytics data model?

a) Interactions > Users > Sessions
b) Sessions > Users > Interactions
c) Users > Sessions > Interactions
d) Sessions > Visitors > Interactions

"""
PP3 = raw_input("Please enter your answer: ")

if PP3 == "c" or PP3 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif PP3=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is C."
    incorrect_answers = incorrect_answers + 1




print
print"""PP4. Google Analytics is able to measure if a user is a first time visitor or repeat visitor.

a) True
b) False
"""
PP4 = raw_input("Please enter your answer: ")

if PP4 == "a" or PP4 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif PP4=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1




print
print"""PP5.  Which of the following are "hit" types tracked by Google Analytics?


a) Pageviews
b) Reservations
c) Events
d) Transactions
e) All of the above
f) None of the above
g) a, b, c
h) a, c, d
i) b, c, d
"""
PP5 = raw_input("Please enter your answer: ")

if PP5 == "h" or PP5 == "H":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif PP5=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is H) Pageviews, Events, Transactions."
    incorrect_answers = incorrect_answers + 1

#2.1 Data Collection Overview
print
print"""PP6. The tracking code in Google Analytics:

a) connects data to your specific Google Analytics account
b) sends data back to your Google Analytics account for reporting
c) tracks changes in your AdWords account
d) identifies new and returning users
e) All of the above
f) a, b, c
g) a, b, d
h) a, c, d
i) b, c, d
"""
PP6 = raw_input("Please enter your answer: ")

if PP6 == "g" or PP6 == "G":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif PP6=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is G."
    incorrect_answers = incorrect_answers + 1 



print
print"""PP7. The same type of Google Analytics tracking code should be used for both a website and a mobile app.

a) True
b) False

"""
PP7 = raw_input("Please enter your answer: ")

if PP7 == "b" or PP7 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif PP7=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is B) False."
    incorrect_answers = incorrect_answers + 1 


#2.2 Website Data Collection
print
print"""PP8.  You should include Google Analytics tracking code on every page of a website you want to track.

a) True
b) False

"""
PP8 = raw_input("Please enter your answer: ")

if PP8 == "a" or PP8 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif PP8=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is A) True."
    incorrect_answers = incorrect_answers + 1 


print
print"""PP9.Where does the Google Analytics tracking code belong?

a) After the closing </head> tag in your HTML
b) Before the closing </head> tag in your HTML
c) After the closing </body> tag in your HTML
d) Before the closing </body> tag in your HTML

"""
PP9 = raw_input("Please enter your answer: ")

if PP9 == "b" or PP9 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif PP9=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is B."
    incorrect_answers = incorrect_answers + 1 



print
print"""PP10.  In order to distinguish between users on web pages, Google Analytics:

a) uses the IP address of a device that accesses the site
b) uses the city, state and country of a visitor that access the site
c) creates anonymous unique identifiers using third-party cookies
d) creates anonymous unique identifiers using first-party cookies
"""
PP10 = raw_input("Please enter your answer: ")

if PP10 == "d" or PP10 == "D":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif PP10=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is D."
    incorrect_answers = incorrect_answers + 1 


#2.3 Mobile app data collection

print
print"""PP11. For mobile applications, Google Analytics will use the same Javascript tracking code as websites.

a) True
b) False
"""
PP11 = raw_input("Please enter your answer: ")

if PP11 == "b" or PP11 == "B":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif PP11=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is B) False."
    incorrect_answers = incorrect_answers + 1 


print
print"""PP12. Google Analytics stores mobile app usage data locally on the device and sends it to the Analytics account later using a batch process called:

a) resending
b) rerouting
c) dispatching
d) displacing
"""
PP12 = raw_input("Please enter your answer: ")

if PP12 == "c" or PP12 == "C":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif PP12=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is C) dispatching"
    incorrect_answers = incorrect_answers + 1 


print
print"""PP13.  If an app gets uninstalled and then reinstalled, Google Analytics will have to create a new unique identifier on the device instead of matching the session as coming from a returning user.

a) True
b) False
"""
PP13 = raw_input("Please enter your answer: ")

if PP13 == "a" or PP13 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif PP13=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1 


#2.4 Measurement Protocol Data

print
print"""PP14.  The measurement protocol can collect and send user activity data to Google Analytics from any web-connected device, such as a ticket kiosk.

a) True
b) False
"""
PP14 = raw_input("Please enter your answer: ")

if PP14 == "a" or PP14 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif PP14=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is A) True."
    incorrect_answers = incorrect_answers + 1 



print
print"""PP15.  Similar to the JavaScript and mobile SDKs, you’ll need to include a tracking ID with each hit collected by the Measurement Protocol.

a) True
b) False
"""
PP15 = raw_input("Please enter your answer: ")

if PP15 == "a" or PP15 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif PP15=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is A) True."
    incorrect_answers = incorrect_answers + 1 



#3.1 Proccessing & configuration overview

print
print"""PP16. 
"""
PP16 = raw_input("Please enter your answer: ")

if PP16 == "a" or PP16 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif PP16=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1 



print
print"""PP17. 
"""
PP17 = raw_input("Please enter your answer: ")

if PP17 == "a" or PP17 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif PP17=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1 


print
print"""PP18. 
"""
PP18 = raw_input("Please enter your answer: ")

if PP18 == "a" or PP18 == "A":
    print "correct!"
    correct_answers = correct_answers + 1
    
elif PP18=="s":
    print "go to to next question."
    skipped = skipped + 1 
        
else:
    print "sorry, incorrect. the answer is A."
    incorrect_answers = incorrect_answers + 1 








print
print
time.sleep(5)
print "Those are all the questions."

print
print
time.sleep(2)


print "Wow", name + ",", "you're done!"
print "Time for the scoring."




print "The total number of questions were", total
print "Number of correct answers:", correct_answers
print "Number of wrong answers:", incorrect_answers
print "Number of skipped questions:", skipped
print

try:
    score = int((correct_answers/total) * 100)

    print score,"%","score achieved" 

    print
    if score >= 78:
        print "Congratulations, You are ready to take the Google Analytics IQ Certification Exam."
    else:
        print "You may want to complete more practice questions before attempting the Google Analytics IQ Certification Exam."
    
except:
    print int((correct_answers/171) * 100),"%", "score achieved"
    if score >= 78:
        print "Congratulations, You are ready to take the Google Analytics IQ Certification Exam."
    else:
        print "You may want to complete more practice questions before attempting the Google Analytics IQ Certification Exam."  
    
print "Thank you for completing the Google Analytics Practice Program."
print "Have a nice day & good luck"

