import random
print("Welcome to random string compiler! Shortly you will be asked to enter a string that will be jumbled, please prepare yourself, mentally")
liemscue = input("String: ")
banan = []
for x in liemscue:
    banan.append(x)
otherbanan = []
cheesydj = 89
while len(banan) != len(otherbanan):
    cheesydj = random.randrange(0, len(banan))
    if cheesydj not in otherbanan:
        otherbanan.append(cheesydj)
obelisk = []
for x in otherbanan:
    obelisk.append(banan[x])
for x in obelisk:
    print(x, end="")
