"""
In a small town the population is p0 = 1000 at the beginning of a year. The population regularly increases by 2 percent
per year and moreover 50 new inhabitants per year come to live in the town. How many years does the town need to see its
population greater or equal to p = 1200 inhabitants?

p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)

the function nb_year should return n number of entire years needed to get a population greater or equal to p.

aug is an integer, percent a positive or null number, p0 and p are positive integers (> 0)

Return n (number of years)
"""

def nb_year(p0, percent, aug, p):
    n = 0
    pop = 0
    while pop < p:
        pop = p0 + p0 * (percent/100) + aug
        p0 = pop
        n += 1
    return n

print(nb_year(1000, 2, 50, 1200))

"""
Solution: 

def nb_year(population, percent, aug, target):
    year = 0
    while population < target:
        population += population * percent / 100. + aug
        year += 1
    return year
"""