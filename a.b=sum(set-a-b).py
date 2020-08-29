"""
A friend of mine takes a sequence of numbers from 1 to n (where n > 0).
Within that sequence, he chooses two numbers, a and b.
He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.
Given a number n, could you tell me the numbers he excluded from the sequence?
"""
# 102, 110, 1006, 446, 846, 1000003
import datetime


def removNb(n):
    def mult(num, *args):
        nonlocal c, s
        global a, b
        for d in args:
            v = num * d
            if v == (s - (num + d)):
                a = num
                b = d
                return a, b
    c = [x for x in range(1, n + 1)]
    s = sum(c)
    for num in c:
        mult(num, *c)
    try:
        a, b
    except NameError:
        return []
    else:
        return [(b, a), (a, b)]


i = datetime.datetime.now()
print(removNb(1006))
f = datetime.datetime.now()
print(f - i)


"""

Other Version:

def removNb(n):
    a = None
    b = None
    c = list(range(1, n + 1))
    s = sum(c)
    for num in c:
        for d in c:
            v = num * d
            m = (s - (num + d))
            if v == m:
                a = num
                b = d
    if a is None and b is None:
        return []
    else:
        return ([(b, a), (a, b)])
        
        
Codewars Solution:

def removNb(n):
    total = n*(n+1)/2
    sol = []
    for a in range(1,n+1):
        b = (total-a)/(a+1.0)
        if b.is_integer() and b <= n:
            sol.append((a,int(b)))
    return sol
"""
