#sorting a random number from lowest to highest

import random
import math

numlist = []
for i in range(10):
    numlist.append(random.randrange(1,101))
i = 0
while i < len(numlist) - 1:
    j = len(numlist) - 1
    while j > i:
        if (numlist[j] < numlist[j - 1]):
            temp = numlist[j]
            numlist[j] = numlist[j - 1]
            numlist[j - 1] = temp
        j -= 1
    i += 1
print(numlist)
