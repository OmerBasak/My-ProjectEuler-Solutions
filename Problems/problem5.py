"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder. 

What is the smallest positive number that is evenly divisible divisible with no remainder by all of the numbers from 1 to 20?
"""

numbers = list(range(1,20))

fList = []

count = 2
while True:
    if count > sorted(numbers, reverse=True)[0]: break
    newNumbers = []
    ekle = False
    for i in range(0, len(numbers)):
        if numbers[i] % count == 0:
            newNumbers.append(int(numbers[i] / count))
            ekle = True
        else: newNumbers.append(numbers[i])
    if ekle == True: fList.append(count)
    numbers = newNumbers

    gec = False
    for i in range(0, len(numbers)):
        if numbers[i] % count == 0: gec = True
    if gec == False: count+=1
    
result = 1
for f in fList: result*=f
print("result: " + str(result))