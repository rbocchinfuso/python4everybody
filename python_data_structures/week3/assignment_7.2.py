## 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:

## X-DSPAM-Confidence:    0.8475

## Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
## You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

# Assignment 7.2
# Use the file name mbox-short.txt as the file name
#fname = 'mbox-short.txt'
fname = raw_input("Enter file name: ")
fh = open(fname)
x = 0
y = 0
n = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print line
    startpos = line.find(' ')
    #print line.strip()[startpos:]
    x = line.strip()[startpos:]
    y = float(x) + float(y)
    n = n + 1
    #print n
#print float(y)
#print n
avg = float(y) / n
print 'Average spam confidence:',avg
#print "Done"