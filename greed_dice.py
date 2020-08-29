"""
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw
according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet
(contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
"""
from collections import Counter
def score(dice):
    a = Counter(dice)
    sco = 0
    for num, times in a.items():
        if num == 1:
            if times < 3:
                sco += 100*times
            elif times == 3:
                sco += 1000
            else:
                sco += (1000 + 100*(times-3))
        elif num == 2:
            if times >= 3:
                sco += 200
        elif num == 3:
            if times >= 3:
                sco += 300
        elif num == 4:
            if times >= 3:
                sco += 400
        elif num == 5:
            if times < 3:
                sco += 50*times
            elif times == 3:
                sco += 500
            else:
                sco += (500 + 50 * (times-3))
        elif num == 6:
            if times >= 3:
                sco += 600
    return sco

print(score([2, 3, 4, 6, 2]))

"""
Codewars:

def score(dice): 
  sum = 0
  counter = [0,0,0,0,0,0]
  points = [1000, 200, 300, 400, 500, 600]
  extra = [100,0,0,0,50,0]
  for die in dice: 
    counter[die-1] += 1
  
  for (i, count) in enumerate(counter):
    sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)
    

def score(dice):
    return dice.count(1)//3 * 1000 + dice.count(1)%3 * 100 \
           + dice.count(2)//3 * 200 \
           + dice.count(3)//3 * 300 \
           + dice.count(4)//3 * 400 \
           + dice.count(5)//3 * 500 + dice.count(5)%3 * 50 \
           + dice.count(6)//3 * 600 \
"""