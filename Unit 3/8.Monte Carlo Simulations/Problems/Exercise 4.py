import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    count = 0
    for i in range(numTrials):
        dict = {'red':3, 'green':3}
        numbals = 6
        for i in range(3):
            ball = random.random()
            probred = dict['red'] / numbals
            probgreen = dict['green'] / numbals
            numbals -= 1
            if ball <= probred:
                dict['red'] = dict['red'] - 1
            else:
                dict['green'] = dict['green'] - 1
        if dict['red'] == 0 or dict['green'] == 0:
            count += 1
    result = count/numTrials
    return result

print(noReplacementSimulation(5000))