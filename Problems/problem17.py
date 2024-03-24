"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3+3+5+4+4=19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

# Soruyu okuyunca aklıma iki farklı yol geldi. İki yolu da denemek istiyorum.

"""
# My First Solution
ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
x1 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
x2 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

sum = 0
for s in ones: sum+=len(s)
for f in x1: sum+=len(f)

for m in x2:
    sum+=len(m)
    for s in ones: sum+=len(m+s)

for s in ones:
    sum+=len(s+"hundred")
    s+="hundredand"
    for f in ones: sum+=len(s+f)
    for g in x1: sum+=len(s+g)
    for m in x2:
        sum+=len(s+m)
        for x in ones: sum+=len(s+m+x)

sum+=len("onethousand")

print("result: " + str(sum))
"""

# My Second Solution;
first = [3, 3, 5, 4, 4, 3, 5, 5, 4] # [1-9]
second = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8] # [10-19]
tens = [6, 6, 5, 5, 5, 7, 6, 6] # [20,30,40,50,60,70,80,90]
hAnd, h = len("hundredand"), len("hundred")

sum = 0
for f in first: sum+=f
for f in second: sum+=f

for ten in tens:
    sum+=ten
    for f in first: sum+=ten+f

for f in first:
    sum+=f+h
    f+=hAnd
    for f2 in first: sum+=f+f2
    for s in second: sum+=f+s
    for t in tens:
        sum+=f+t
        for f3 in first: sum+=f+t+f3

sum+=len("onethousand")

print("result: " + str(sum))