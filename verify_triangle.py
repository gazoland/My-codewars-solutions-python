"""
Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with
the sides of given length and false in any other case.
"""

def is_triangle(a, b, c):
    if a + b > c:
        if b + c > a:
            if a + c > b:
                return True
            else: return False
        else: return False
    else: return False


print(is_triangle(7,2,2))


"""
Solution:

def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)
    
Retorna direto um boolean
"""