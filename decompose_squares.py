"""
https://www.codewars.com/kata/54eb33e5bc1a25440d000891/train/python

My little sister came back home from school with the following task: given a squared sheet of paper she has to cut it
in pieces which, when assembled, give squares the sides of which form an increasing sequence of numbers. At the
beginning it was lot of fun but little by little we were tired of seeing the pile of torn paper. So we decided to write
a program that could help us and protects trees.

Task
Given a positive integral number n, return a strictly increasing sequence (list/array/string depending on the language)
of numbers, so that the sum of the squares is equal to n².

If there are multiple solutions (and there will be), return as far as possible the result with the largest possible
values:

Examples
decompose(11) must return [1,2,4,10]. Note that there are actually two ways to decompose 11²
11² = 121 = 1 + 4 + 16 + 100 = 1² + 2² + 4² + 10² but don't return [2,6,9], since 9 is smaller than 10.

For decompose(50) don't return [1, 1, 4, 9, 49] but [1, 3, 5, 8, 49] since [1, 1, 4, 9, 49] doesn't form a strictly
increasing sequence.

Note
Neither [n] nor [1,1,1,…,1] are valid solutions. If no valid solution exists, return nil, null, Nothing,
None (depending on the language) or "[]" (C) ,{} (C++), [] (Swift, Go).

The function "decompose" will take a positive integer n and return the decomposition of N = n² as:

[x1 ... xk] or
"x1 ... xk" or
Just [x1 ... xk] or
Some [x1 ... xk] or
{x1 ... xk} or
"[x1,x2, ... ,xk]"
"""
import itertools, datetime


def decompose(n):
    class BreakIt(Exception): pass
    g = []
    a = []
    c = [u for u in range(n-1,0,-1)]
    count = 0
    m = (itertools.combinations(c,m) for m in range(6,1,-1))
    for v in m:
        for h in v:
            if sum(k*k for k in h) == n*n:
                if count >= 1:
                    if h[0] <= g[-1][0]:
                        break
                    if h[1] <= g[-1][1]:
                        break
                g.append(h)
                if len(g[0]) == 6:
                    break
                if count == 0:
                    count += 1
        break
    print(g)
    if len(g) == 1:
        return list(g[0])
    elif len(g) > 1:
        for j in g:
            a.append(max(j))
    for j in g:
        if max(a) in j:
            return list(j)


z = datetime.datetime.now()
print(decompose(80))
print(datetime.datetime.now()-z)



"""
Not fast enough...  ):


Orginial try:
import itertools
def decompose(n):
    g = []
    a = []
    c = [u for u in range(2,n)]
    for m in range(2,8):
        v = itertools.combinations(c,m)
        for h in v:
            if sum(k*k for k in h) == n*n:
                g.append(list(h))
    if len(g) == 1:
        return g[0]
    elif len(g) > 1:
        for j in g:
            a.append(max(j))
    for j in g:
        if max(a) in j:
            return j
"""