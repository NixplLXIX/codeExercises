x = "dada"
y = "amam"
items = ["rock", "paper", "scissors"]
xx = "8"
yy = "32"
xtrue = False
ytrue = False
while x != "":
    if xtrue == False and xx != "":
        x = input("P1: ")
        xx = x.lower()
        if xx not in items and xx != "":
            print("Skill issue detected with Player 1, please try again.")
            continue
    xtrue = True
    if ytrue == False and yy != "":
        y = input("P2: ")
        yy = y.lower()
        if yy not in items and yy != "":
            print("Skill issue detected with Player 2, please try again.")
            continue

    ytrue = True

    if xx in items and yy in items:
        ytrue = False
        xtrue = False
        if xx == "rock" and yy == "scissors":
            print("Player 1 wins")
        if xx == yy and xx != "" and yy != "":
            print("Tie")
        if xx == "scissors" and yy == "rock":
            print("Player 2 wins")
        if xx == "paper" and yy == "rock":
            print("Player 1 wins")
        if yy == "paper" and xx == "rock":
            print("Player 2 wins")
        if xx == "scissors" and yy == "paper":
            print("Player 1 wins")
        if yy == "scissors" and xx == "paper":
            print("Player 2 wins")
print("Thank for using this game. Have a good day.")
