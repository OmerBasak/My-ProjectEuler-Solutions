"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

def asalKontrol(n):
    asal = True
    for i in range(2, n):
        if n%i == 0: asal = False
    return asal

first = num = 600851475143
x = []

while True:
    count = 3
    while True:
        if asalKontrol(count): 
            if num%count == 0: break
        count+=1

    x.append(count)
    num = num/count

    mx = 1
    for a in x: mx*=a

    if mx == first:
        break

x = list(sorted(x, reverse=True))
print("result: " + str(x[0]))