
import random
# This program generates all the four digit numbers from 0 to 9, in all the possible combinations and write to a file.
# 1234, 1235, .....
passlist = []

'''while len(passlist) < 100:
    x = random.randrange(00, 99)
    y = str(x)
    if len(y) < 2:
        y = "0"+y
    if y not in passlist:
        passlist.append(y)
    print(y)
print(len(passlist))'''

f = open("tries.txt", "w")
for x in range(10000):
    y = str(x)
    numberOfZeroes = 0
    if len(y) == 1:
        numberOfZeroes = 3
    if len(y) == 2:
        numberOfZeroes = 2
    if len(y) == 3:
        numberOfZeroes = 1
    y = "0" * numberOfZeroes + y
    if y not in passlist:
        passlist.append(y)
        f.write(y)
        f.write("\n")
f.close()
