from email.contentmanager import raw_data_manager
import random
x = input("(insert comma) Pick Number Parameters: ")
howManyNumbersYouWant = int(
    input("How many different random number do you want? "))
Disco = x.split(",")
Lyem = []
for l in Disco:
    y = int(l)
    Lyem.append(y)
jorgi = []
while len(jorgi) != howManyNumbersYouWant:
    random1 = random.randint(Lyem[0], Lyem[1])
    if (random1 not in jorgi):
        jorgi.append(random1)
for j in jorgi:
    print(j)
