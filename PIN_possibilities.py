"""
Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to
a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an
electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

The keypad has the following layout:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another
adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And
instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally
lock the system or sound the alarm. That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in
Java and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs
(get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results, must be
strings, because of potentially leading '0's. We already prepared some test cases for you.

Detective, we count on you!
"""
import datetime


def get_pins(observed):
    m = []
    v = []
    k = 0
    a = ['1', '2', '4']
    b = ['1', '2', '3', '5']
    c = ['2', '3', '6']
    d = ['1', '4', '5', '7']
    e = ['2', '4', '5', '6', '8']
    f = ['3', '5', '6', '9']
    g = ['4', '7', '8']
    h = ['5', '7', '8', '9', '0']
    i = ['6', '8', '9']
    j = ['0', '8']
    D = {'0': j, '1': a, '2': b, '3': c, '4': d, '5': e, '6': f, '7': g, '8': h, '9': i}
    for x in observed:
        m.append(D[x])
    if len(observed) == 1:
        for y in m[0]:
            v.append(y)
    elif len(observed) == 2:
        for y in m[0]:
            for x in m[1]:
                v.append(y+x)
    elif len(observed) == 3:
        for y in m[0]:
            for x in m[1]:
                for z in m[2]:
                    v.append(y+x+z)
    elif len(observed) == 4:
        for y in m[0]:
            for x in m[1]:
                for z in m[2]:
                    for w in m[3]:
                        v.append(y+x+z+w)
    elif len(observed) == 5:
        for y in m[0]:
            for x in m[1]:
                for z in m[2]:
                    for w in m[3]:
                        for t in m[4]:
                            v.append(y+x+z+w+t)
    elif len(observed) == 6:
        for y in m[0]:
            for x in m[1]:
                for z in m[2]:
                    for w in m[3]:
                        for t in m[4]:
                            for u in m[5]:
                                v.append(y+x+z+w+t+u)
    elif len(observed) == 7:
        for y in m[0]:
            for x in m[1]:
                for z in m[2]:
                    for w in m[3]:
                        for t in m[4]:
                            for u in m[5]:
                                for s in m[6]:
                                    v.append(y+x+z+w+t+u+s)
    elif len(observed) == 8:
        for y in m[0]:
            for x in m[1]:
                for z in m[2]:
                    for w in m[3]:
                        for t in m[4]:
                            for u in m[5]:
                                for s in m[6]:
                                    for r in m[7]:
                                        v.append(y+x+z+w+t+u+s+r)
    return v

# Second solution:
def pin(obs):
    m = []
    v = []
    k = 0
    a = ['1', '2', '4']
    b = ['1', '2', '3', '5']
    c = ['2', '3', '6']
    d = ['1', '4', '5', '7']
    e = ['2', '4', '5', '6', '8']
    f = ['3', '5', '6', '9']
    g = ['4', '7', '8']
    h = ['5', '7', '8', '9', '0']
    i = ['6', '8', '9']
    j = ['0', '8']
    D = {'0': j, '1': a, '2': b, '3': c, '4': d, '5': e, '6': f, '7': g, '8': h, '9': i}
    for x in obs:
        m.append(D[x])
    for y in m[0]:
        if len(obs) == 1:
            v.append(y)
            continue
        for x in m[1]:
            if len(obs) == 2:
                v.append(y + x)
                continue
            for z in m[2]:
                if len(obs) == 3:
                    v.append(y + x + z)
                    continue
                for w in m[3]:
                    if len(obs) == 4:
                        v.append(y + x + z + w)
                        continue
                    for t in m[4]:
                        if len(obs) == 5:
                            v.append(y + x + z + w + t)
                            continue
                        for u in m[5]:
                            if len(obs) == 6:
                                v.append(y + x + z + w + t + u)
                                continue
                            for s in m[6]:
                                if len(obs) == 7:
                                    v.append(y + x + z + w + t + u + s)
                                    continue
                                for r in m[7]:
                                    v.append(y + x + z + w + t + u + s + r)
    return v


time = datetime.datetime.now()
print(get_pins('25885743'))
print(time-datetime.datetime.now())
time = datetime.datetime.now()
print(pin('25885743'))
print(time-datetime.datetime.now())

"""
Codewars Solution:
from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
"""