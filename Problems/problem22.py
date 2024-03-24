"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 X 53 = 49714.

What is the total of all the name scores in the file?
"""

# Not: Parçalamayı çift kelimeli ismin olmadığı varsayarak yaptım. Diğer türlü farklı bir yöntem kullanmam gerekirdi.
import string
harfListesi = string.ascii_uppercase

names = open("names.txt", "r").read()
names = names.replace('","', ' ').replace('"', '').split(" ")
names.sort()

total = 0
for i in range(0, len(names)):
    name = names[i]
    value = 0
    for n in name: value+=harfListesi.find(n) + 1
    point = value*(i+1) # i+1 name'in liste sırası
    total+=point
print("result: " + str(total))