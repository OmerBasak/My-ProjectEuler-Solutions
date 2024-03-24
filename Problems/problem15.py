"""
Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20 x 20 grid?

"""

#Tekrarlı Permütasyon

import math
row = 20
column = 20

toplamAdim = row+column
r = row

asama = math.factorial(toplamAdim) / (math.factorial(r) * math.factorial(toplamAdim-r))

print("result: " + str(int(asama)))