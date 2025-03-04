

zora = input("Good Thing for Strangey: ")
if zora != "":

    StrangeyList = zora.split(",")
if zora != "" or zora == "":
    zeneas = input("Would you like to add good thing for other kid? y/n: ")
if zeneas == "y" or "Y":
    yunobo = input("Good Thing For Lovisa: ")
if yunobo != "":
    LovisaList = yunobo.split(",")
LovisaScore = len(LovisaList)
StrangeyScore = len(StrangeyList)
if len(LovisaList) > 0:
    print("Good Thing(s) for Lovisa: ")
    for x in LovisaList:
        print(x+",")
    print("Total Good Thing(s):", LovisaScore)
if len(StrangeyList) > 0:
    print("Good Thing(s) for Strangey: ")
    for x in StrangeyList:
        print(x+",")
    print("Total Good Thing(s):", StrangeyScore)
