"""7.2 Write a program that prompts for a file name, 
then opens that file and reads through the file, 
looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the 
floating point values from each of 
the lines and compute the average of those
 values and produce an output as shown below.
You can download the sample data at
 http://www.pythonlearn.com/code/mbox-short.txt
when you are testing below enter mbox-short.txt
as the file name."""

   
fname = raw_input("Enter file name: ")
fhand = open(fname)
count = 0
sum = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    print line
    firstpos = line.find(':')
    print firstpos
    print len(line)
    print line[firstpos + 1:]
    num = float(line[firstpos+1:])
    print num, type(num)
    count = count + 1
    sum = sum + num
    average = sum/count
    print average


print 'Line Count:',count
print 'Average spam confidence:', average


##CODE SUBMITTED FOR GRADE###
fname = raw_input("Enter file name: ")
fhand = open(fname)
count = 0
sum = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:") : continue   
    firstpos = line.find(':')       
    num = float(line[firstpos+1:])   
    count = count + 1
    sum = sum + num
    average = sum/count
    
print 'Average spam confidence:', average




   



    

       
   


