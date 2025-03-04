import random
file1=open("namelist.txt")
randomizernames = file1.read()
randomizernames2 = randomizernames.split()
intialnames = input("Name(s) (Whatever you want): ")
intialnameslowered = intialnames
inputnames = intialnameslowered.split(" ")
EndNumber="nasdlkjjasldjaslkdjasld"
termination = ""
counter=0
theName = "qw"
randompart = "no one is going to read this"
while termination != "y":
    theName = random.choice(inputnames)
    randompart = random.choice(randomizernames2)
    EndNumber=str(random.randint(1,9999))
    if counter == 0:
        termination="n"
        print(theName+randompart+EndNumber)
    elif counter >= 1:
        termination=input("Are you satisfied(y/n)? ")
        if termination != "y":    
            print(theName+randompart+EndNumber)
        else:
            pass
    if termination == "y":
        counter=counter-1
        counter=counter+1
    else:
        counter=counter+1
        
    
print("You have generated a name", counter, "time(s)")
    
    


