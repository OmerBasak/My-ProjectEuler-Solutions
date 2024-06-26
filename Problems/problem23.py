"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

"""
--> Bir isAbundant fonksiyonu oluşturup soruyu progTürkçeleştirdim;
isAbundant(x) == isAbundant(y) == True ise
x+y'nin alamayacagi sayilarin toplami kactir?
Not: x+y, 28123'den buyuk tüm sayilari alabilir.
"""


def isAbundant(n):
    sum = 0
    for i in range(1, int((n/2)+1)):
        if n%i == 0: sum+=i
    if sum > n: return True
    else: return False


Abundants = []
for i in range(1, 28124):
    if isAbundant(i): Abundants.append(i)


toplam = []
for x in Abundants:
    for y in Abundants:
        if x+y < 28124: toplam.append(x+y)  
toplam = list(set(toplam))

def binary_search(arr, target): # Biraz araştırınca bu algoritmaya ulaştım.
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

missing_numbers = []
for num in range(1, 28124):
    if binary_search(toplam, num) == -1:
        missing_numbers.append(num)

sum = 0
for i in missing_numbers: sum+=i
print("result: " + str(sum))