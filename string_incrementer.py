"""
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100
"""


def increment_string(strng):
    def adds():
        s = strng
        aux = ''
        for u in strng[::-1]:
            if u.isdigit():
                aux += u
            else:
                break
        for _ in range(len(aux)):
            s = s[:-1]
        a = aux[::-1]
        b = (str(int(a) + 1))
        return s + b.zfill(len(aux) + 1) if a[-1] == '9' else s + b.zfill(len(aux))

    if strng == '':
        return '1'
    elif not strng[-1].isnumeric():
        return strng + '1'
    else:
        return adds()


print(increment_string('fooob99'))

"""
Codewars Solution:

def increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))
"""