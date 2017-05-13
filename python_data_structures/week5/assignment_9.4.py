## 9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

# Assignment 9.4
fname = 'mbox-short.txt'
#name = raw_input("Enter file:")
if len(fname) < 1 : name = "mbox-short.txt"
fh = open(fname)

#print 'Debug:', fname
fh = open(fname)
count = 0
maillist = list()

for line in fh:
    #print line.rstrip()
    words = line.split()
    #print 'Debug:', words
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    maillist.append(words[1])

#print 'Debug:', maillist[:]

d = dict()
for email in maillist:
    #print 'Debug:', email
#    if email not in d:
#        d[email] = 1
#    else:
#        d[email] += 1
    d[email] = d.get(email,0) +1       
#print 'Debug:', d


count = d.values()
#print 'Debug:', count
m = max(count)
#print 'Debug:', m


for email in d:
    if d[email] >= m:
        print email, d[email]
