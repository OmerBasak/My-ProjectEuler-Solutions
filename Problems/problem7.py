"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
import math

def asalKontrol(n):
    asal = True
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0: asal = False
    return asal

i = 3
count = 1
while True:
    if asalKontrol(i) == True: 
        count+=1
        if count == 10001: 
            print("result: " + str(i))
            break
    i+=2 # Çift sayıları atladım