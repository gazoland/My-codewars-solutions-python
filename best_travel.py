"""

https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa/train/python

John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper a list of distances between
these towns. ls = [50, 55, 57, 58, 60]. John is tired of driving and he says to Mary that he doesn't want to drive more
than t = 174 miles and he will visit only 3 towns.

Which distances, hence which towns, they will choose so that the sum of the distances is the biggest possible to please
Mary and John?

Example:

With list ls and 3 towns to visit they can make a choice between: [50,55,57],[50,55,58],[50,55,60],[50,57,58],
[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60].

The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

The biggest possible sum taking a limit of 174 into account is then 173 and the distances of the 3 corresponding towns
is [55, 58, 60].

The function chooseBestSum (or choose_best_sum or ... depending on the language) will take as parameters t (maximum sum
of distances, integer >= 0), k (number of towns to visit, k >= 1) and ls (list of distances, all distances are positive
or null integers and this list has at least one element). The function returns the "best" sum ie the biggest possible
sum of k distances less than or equal to the given limit t

[91, 74, 73, 85, 73, 81, 87]
"""

# Sem o módulo itertools:
def choose_best_sum(t, k, ls):
    try:
        aux = [[[ls[m] for m in range(0, len(ls))] for _ in range(k)] for _ in range(k)]
        res = []
        s = set()
        i = 0
        while i != k:
            j = 0
            while j != k:
                z = []
                for _ in range(0, j):
                    aux[i][j].pop(1)
                for _ in range(0, k - 1):
                    z.append(aux[i][j][0])
                    aux[i][j].pop(0)
                    if len(aux[i][j]) == 0:
                        break
                if len(aux[i][j]) > 0:
                    p = sum(z)
                    res.append([p + x for x in aux[i][j]])
                j += 1
            i += 1
            for c in range(i, k):
                for b in range(0, k):
                    aux[c][b].pop(0)
        for g in res:
            for d in g:
                if d <= t:
                    s.add(d)
    except IndexError:
        return None
    try:
        max(s)
    except ValueError:
        return None
    except IndexError:
        return None
    else:
        return max(s)


print(choose_best_sum(331,4,[91, 74, 73, 85, 73, 81, 87]))


# CODEWARS SOLUTION:
"""
import itertools
def choose_best(t, k, ls):
    try:
        return max(sum(i) for i in itertools.combinations(ls,k) if sum(i)<=t)
    except:
        return None
"""

"""
---------------------------- Base for function

ls = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
k = 8
i = 0
t = 430
aux = [[[ls[m] for m in range(0, len(ls))] for _ in range(k)] for _ in range(k)]
res = []
s = set()
while i != k:
    j = 0
    while j != k:
        z = []
        for _ in range(0,j):
            aux[i][j].pop(1)
        for _ in range(0,k-1):
            z.append(aux[i][j][0])
            aux[i][j].pop(0)
            if len(aux[i][j]) == 0:
                break
        if len(aux[i][j]) > 0:
            p = sum(z)
            res.append([p + x for x in aux[i][j]])
        j += 1
    i += 1
    for c in range(i,k):
        for b in range(0,k):
            aux[c][b].pop(0)
for g in res:
    for d in g:
        if d <= t:
            s.add(d)
#print(res)
#print(max(s))

"""


"""
---------------------------- Base algorithm

res = []
ls = [91, 74, 73, 81, 88]
aux = [[91, 74, 73, 81, 88], [91, 74, 73, 81, 88], [91, 74, 73, 81, 88]]
print(aux)
# 1st iteration:
aux[0].pop(0)
aux[0].pop(0)
res.append([ls[0] + ls[1] + x for x in aux[0]])

# 2nd iteration:
aux[0].pop(0)
res.append([ls[0] + ls[2] + x for x in aux[0]])

# 3rd iteration:
aux[0].pop(0)
res.append([ls[0] + ls[3] + x for x in aux[0]])

# second first:
aux[1].pop(0)
aux[1].pop(0)
aux[1].pop(0)
res.append([ls[1] + ls[2] + x for x in aux[1]])

# second second:
aux[1].pop(0)
res.append([ls[1] + ls[3] + x for x in aux[1]])

# third first:
aux[2].pop(0)
aux[2].pop(0)
aux[2].pop(0)
aux[2].pop(0)
res.append([ls[2] + ls[3] + x for x in aux[2]])

print(res)

m = [ls[0]+ls[1]+ls[2],ls[0]+ls[1]+ls[3],ls[0]+ls[1]+ls[4],ls[0]+ls[2]+ls[3],ls[0]+ls[2]+ls[4],ls[0]+ls[3]+ls[4],ls[1]+ls[2]+ls[3],ls[1]+ls[2]+ls[4],ls[1]+ls[3]+ls[4],ls[2]+ls[3]+ls[4]]
print(m)
print(set(m))


---------------------------- First function working for 1 example
def choose_best_sum(t, k, ls):
    tu = tuple(ls)
    aux = [tu for _ in range(k)]
    res = []
    i = 0
    s = set()
    while i != k:
        aux[i] = list(aux[i])
        for m in range(0, i + 1):
            aux[i].pop(0)
        for j in range(1, k + 1 - i):
            aux[i].pop(0)
            res.append([ls[i] + ls[i + j] + x for x in aux[i]])
        i += 1
    for g in res:
        for d in g:
            if d <= t:
                s.add(d)
    print(res)
    return max(s)

print(choose_best_sum(245,3,[91, 74, 73, 81, 88]))
"""
