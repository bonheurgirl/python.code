def computegrade(score):
    if score >= 1.0:
        return 'Bad Score'
    if score >= 0.9 :
        return 'A'
    elif score >= 0.8 :
        return 'B'
    elif score >= 0.7 :
        return 'C'
    elif score >= 0.6 :
        return 'D'
    elif  score < 0.6 :
        return 'F'

try:
    inp = raw_input ("Enter score between 0.0 and 1.0:")
    score = float(inp)
except:
    print 'Bad score'
    quit ()

score = computegrade (score)
print score