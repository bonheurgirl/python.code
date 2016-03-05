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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
    
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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1

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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1

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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1

print
print """Note: The conversion credit is calculated
as follows: purchase value/touch-points in the
conversion path = 100/4 = 25"""

print
time.sleep(1)
print "Number of Correct Answers So far:", correctanswers

time.sleep(2)
print
print "Next Section:  Metrics & Dimensions"

time.sleep(1)
print """MD1.Which of the following suggests a poorly performing landing page?
a) Bounce Rate > 90%
b) Bounce Rate < 90%
c) % New Visits > 90%
d) % New Visits < 90%
e) None of these answers"""

md1 = raw_input("Please enter your answer: ")

if md1 == "a" or md1 == "A":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
    
    
print
print"""MD2.Which of the following Behavior metrics
shows the number of sessions that included a view of a page?

a) Visits
b) Unique Pageviews
c) Pageviews
d) Bounce rate
e) Unique Visits"""

md2 = raw_input("Please enter your answer: ")

if md2 == "a" or md2 == "A":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1


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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1

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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1

print
print"""MD5.Which of the following are measures of traffic volume?

a) Avg. Time on Site
b) Margin
c) Bounce Rate
d) Visits"""


md5 = raw_input("Please enter your answer: ")

if md5 == "d" or md5 == "D":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
    
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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1

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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1

print
print"""MD9.Which of the following are dimensions?

a) Conversion Rate
b) % New Sessions
c) Bounce Rate
d) Region"""
    
md9 = raw_input("Please enter your answer: ")

if md9 == "d" or md9 == "D":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1


print
print"""MD10. The following are examples of dimensions:

(select all that apply)

a) Traffic source
b) Page name
c) Country
d) Unique visitors
e) a, b, c"""


md10 = raw_input("Please enter your answer: ")

if md10 == "e" or md10 == "E":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1


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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1


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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
    
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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
 
print
print"""MD14. Which of the following metrics would
be most useful in measuring how many conversions were initiated by Paid Search?

a) Assisted Conversion Value
b) First Interaction (Click) Conversions
c) Conversion Rate
d) None of these metrics"""
   
md14 = raw_input("Please enter your answer: ")

if md14 == "b" or md14 == "B":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1


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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1


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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
   
print
print"""MD19. Every metric may be combined with every dimension in Google Analytics.

a) True
b) False"""
 
md19 = raw_input("Please enter your answer: ")

if md19 == "b" or md19 == "B":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
    
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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
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
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    


print
time.sleep(1)
print "Number of Correct Answers So far:", correctanswers

time.sleep(2)
print
print "Next Section:  Google AdWords"

time.sleep(1)

AW1 = raw_input("Please enter your answer: ")

if AW1 == "e" or AW1 == "E":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1



AW2 = raw_input("Please enter your answer: ")

if AW2 == "e" or AW2 == "E":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
AW3 = raw_input("Please enter your answer: ")

if AW3 == "e" or AW3 == "E":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
AW4 = raw_input("Please enter your answer: ")

if AW4 == "e" or AW4 == "E":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
AW5 = raw_input("Please enter your answer: ")

if AW5 == "e" or AW5 == "E":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
    
AW6 = raw_input("Please enter your answer: ")

if AW6 == "e" or AW6 == "E":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
    
AW7 = raw_input("Please enter your answer: ")

if AW7 == "e" or AW7 == "E":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    
    
AW8 = raw_input("Please enter your answer: ")

if AW8 == "e" or AW8 == "E":
    print "correct!"
    correctanswers = correctanswers + 1
        
else:
    print "sorry, incorrect."
    incorrectanswers = incorrectanswers + 1
    

print
time.sleep(1)
print "Number of Correct Answers So far:", correctanswers

time.sleep(2)
print
print "Next Section:  "

time.sleep(1)


#from __future__ import division
print "Number of Correct Answers:", correctanswers
print "Number of Wrong Answers:", incorrectanswers
print int((correctanswers/26) * 100),"%", "score achieved"

