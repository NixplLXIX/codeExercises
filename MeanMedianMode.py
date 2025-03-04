def brah():
    import statistics
    import random
    n_num = list(map(float, input(
        "Give me a list of numbers and I will determine the mean and median ").split(",")))
    # MEAN
    n = len(n_num)
    get_sum = sum(n_num)
    mean = get_sum / n
    print("Mean / Average is: " + str(mean))
    # MEDIAN
    n = len(n_num)
    n_num.sort()
    if n % 2 == 0:
        median1 = n_num[n//2]
        median2 = n_num[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = n_num[n//2]
        print("Median is: " + str(median))
        # MODE
        print(n_num)
        print("The maximum occurring element is: ", end="")
        print(statistics.mode(n_num))

    # dice
    n = input("Enter # of dice rolls[1-∞]: ")
    n = int(n)
    diceList = [random.randint(1, 6) for _ in range(0, n)]
    print("\nYou have rolled: ", diceList)


def bruh():
    Who = input("Before this program starts, tell me who you are: ")

    redi = Who.lower()
    if redi == "mr.potiker" or Who == "Mr.Tirpak":
        otherpassword = input("Password: ")
        if otherpassword == "Math_is_cool":
            bruh()

    if redi == "gideon":
        print("Go back scratch. You block code supporter.")
    elif redi == "zaid" or Who == "nickhil" or Who == "jesse":
        gish = input("Password: ")
        if gish == "UwU":
            import statistics
            import random
            n_num = list(map(int, input(
                "Give me a list of numbers and I will determine the mean and median ").split(",")))

            # MEAN
            n = len(n_num)

            get_sum = sum(n_num)
            mean = get_sum / n
            print("Mean / Average is: " + str(mean))
            # MEDIAN
            n = len(n_num)
            n_num.sort()

            if n % 2 == 0:
                median1 = n_num[n//2]
                median2 = n_num[n//2 - 1]
                median = (median1 + median2)/2
            else:
                median = n_num[n//2]
            print("Median is: " + str(median))
            # MODE
            print(n_num)
            print("The maximum occurring element is: ", end="")
            print(statistics.mode(n_num))

            # dice
            n = input("Enter # of dice rolls[1-∞]: ")
            n = int(n)
            diceList = [random.randint(1, 6) for _ in range(0, n)]
            print("\nYou have rolled: ", diceList)

            counter = 0
            # MEAN
            n = len(diceList)

            get_sum = sum(diceList)
            mean = get_sum / n

            print("Mean / Average is: " + str(mean))
            # MEDIAN
            n = len(diceList)
            diceList.sort()

            if n % 2 == 0:
                median1 = diceList[n//2]
                median2 = diceList[n//2 - 1]
                median = (median1 + median2)/2
            else:
                median = diceList[n//2]
            print(diceList)
            print("Median is: " + str(median))
            # MODE
            print("The maximum occurring element is: ", end="")
            print(statistics.mode(diceList))
            # 2 dices
            n = input("Enter # of dice rolls (2 die are rolling) [1-∞]: ")
            n = int(n)
            diceList = [random.randint(2, 12) for _ in range(0, n)]
            print("\nYou have rolled: ", diceList)

            counter = 0
            # MEAN
            n = len(diceList)

            get_sum = sum(diceList)
            mean = get_sum / n

            print("Mean / Average is: " + str(mean))
            # MEDIAN
            n = len(diceList)
            diceList.sort()
            if n % 2 == 0:
                median1 = diceList[n//2]
                median2 = diceList[n//2 - 1]
                median = (median1 + median2)/2
            else:
                median = diceList[n//2]
            print(diceList)
            print("Median is: " + str(median))
            # MODE
            print("The maximum occurring element is: ", end="")
            print(statistics.mode(diceList))
    else:
        tryagain = input("Wrong password, do you want to try again? y/n ")
        while tryagain == "y":
            bruh()
            if tryagain == "n":
                break


bruh()
