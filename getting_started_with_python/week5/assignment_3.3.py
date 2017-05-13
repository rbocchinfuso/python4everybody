# Assignment 3.3
score = raw_input("Enter Score: ")
fscore = float(score);
if fscore >= 0.0 and fscore <= 1.0:
    if fscore >= 0.9: print 'A'
    elif fscore >= 0.8: print 'B'
    elif fscore >= 0.7: print 'C'
    elif fscore >= 0.6: print 'D'
    elif fscore < 0.6: print 'F'
else: print "error"
