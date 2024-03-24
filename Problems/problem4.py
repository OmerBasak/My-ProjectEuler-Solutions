"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def isPalindrome(num):
    palindrome = False
    num = str(num)
    if len(num) % 2 == 0: # Polindrom olabilir.
        count = 0
        st2 = False
        for i in range(len(num)):
            count-=1
            if num[i] != num[count]: st2 = True
        if st2 == False: palindrome = True # Kesin polindrom
    return palindrome

poli = set()
a = range(100, 1000)
for x in a:
    for y in a:
        if isPalindrome(x*y) == True: 
            poli.add(x*y)
            print(x*y)
        
result = sorted(list(poli), reverse=True)
print("Result: " + str(result[0]))