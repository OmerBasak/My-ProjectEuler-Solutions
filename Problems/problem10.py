"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
import math

def asalKontrol(n):
    asal = True
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0: asal = False
    return asal

i = 3
sum = 2
while True:
    if i >= 2000000: break
    if asalKontrol(i) == True: 
        print(i)
        sum+=i
    i+=2
print("result: " + str(sum))

"""
# Eratosthenes Eleği Algoritmasi
def sieve(lim):
    primes = [True] * (lim+1)
    primes[0] = primes[1] = False

    for i in range(2, int(math.sqrt(lim))+1):
        if primes[i]:
            for j in range(i*i, lim+1, i):
                primes[j] = False
    return primes

def sum_primes_to_limit(lim):
    primes = sieve(lim)
    return sum(i for i in range(2,lim+1) if primes[i])
"""