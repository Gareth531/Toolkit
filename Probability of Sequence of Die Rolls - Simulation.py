# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 14:46:50 2018

@author: Gareth Farquharson
"""

import random

def rollDie():
    """returns a random int between 1 and 6"""
    return random.choice([1,2,3,4,5,6])

rollDie()

random.seed(0)
def runSim(goal, numTrials, txt):
    total = 0
    for i in range(numTrials):
        result = ''
        for j in range(len(goal)):
            result += str(rollDie())
        if result == goal:
            total += 1
    print('Actual probability of', txt, '=', round(1/6**len(goal), 8))
    estProbability = round(total/numTrials, 8)
    print('Estimated probability of', txt, '=',round(estProbability, 8))
    
runSim('11111', 1000000, '11111')