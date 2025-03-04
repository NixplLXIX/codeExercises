FrogtheDict = {}
Frog = input("Frog: ")
while Frog:
    if Frog in FrogtheDict:
        FrogtheDict[Frog] = FrogtheDict[Frog] + 1
    else:
        FrogtheDict[Frog] = 1
    Frog = input("Frog: ")
for FrogKey in FrogtheDict:
    print("Frogs that are " + FrogKey +
          "(Even though that's a weird color): " + str(FrogtheDict[FrogKey]))
