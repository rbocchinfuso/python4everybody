## 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
## From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
## Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

# Assignment 10.2

fname = 'mbox-short.txt'
#name = raw_input("Enter file:")
if len(fname) < 1 : name = "mbox-short.txt"
fh = open(fname)

#print 'Debug:', fname
fh = open(fname)

count = dict()

for line in fh:
    line =  line.rstrip()
    if len(line) == 0 : continue
    words = line.split()
    #print 'Debug:', words
    if words[0] != 'From' : continue
    time = words[5].split(":")
    count[time[0]] = count.get(time[0], 0) + 1

d = list()
for key,value in count.items() :
    d.append((key,value))
d.sort()

for hour,count in d :
    print hour, count