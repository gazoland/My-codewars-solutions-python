"""
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"

"""
def accum(s):
    aux = []
    lista = []
    i = 1
    for letter in s:
        aux.append(letter)
    for elem in aux:
        a = (elem * i).title()
        lista.append(a)
        i += 1
    return '-'.join(lista)


s = 'abcd'
print(accum(s))


"""
Solution:

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
"""

