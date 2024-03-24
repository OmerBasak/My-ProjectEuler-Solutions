"""
n! means n x (n - 1) x ... x 3 x 2 x 1.
For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Find the sum of the digits in the number 100!.
"""

# 10 ve katları sayıyının sonuna sadece 0 eklerler. Bu sebepten 10 ve katlarını (5*2)'yi faktöriyel listesinden elemeliyim.
import math

def asalKontrol(n):
    asal = True
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0: asal = False
    return asal

def kacTane(n, m):
    count = 0
    while True:
        if n%m == 0:
            count+=1
            n= n/m
        else: break
    return count


def Bolenler(number: int):
    if asalKontrol(number): return number
    newNumber = ""  
    for i in range(2, number):
        if asalKontrol(i):
            if number % i == 0:
                tane = kacTane(number, i)
                number = number / (i**tane)
                newNumber+=(str(i)+"*")*int(tane)
    if newNumber[-1] == "*": newNumber=newNumber[:-1]
    return newNumber


liste = ""
for i in range(2, 101): liste+=str(Bolenler(i))+"*"
liste = liste[:-1].split("*")
while True:
    if "2" in liste and "5" in liste:
        liste.remove("2")
        liste.remove("5")
    else: break

product = 1
for l in liste: product*=int(l)
sum = 0
for p in str(product): sum+=int(p)
print("result: " + str(sum))