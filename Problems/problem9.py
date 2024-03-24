"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2.

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

toplam = 1000

for i in range(0, int((toplam-3)/3)):
    a = 1+i
    b = a+1
    while True:
        c = 1000 - (a+b)
        if b >= c: break
        if (a**2) + (b**2) == c**2:
            print("result: " + str(a*b*c))
        b+=1