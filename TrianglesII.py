#   Enter a number: 4
#   *******
#    *****
#     ***
#      *
inuit = int(input("Rows: "))
counter = 0
trunk = round(inuit/4)
finalStars = 1
spacecounter = inuit
for x in range(inuit, 1, -1):
    if (counter == 0):
        print(x*" "+'*')
    counter = counter+1
    finalStars = finalStars + 2
    spacecounter = spacecounter-1
    print(((spacecounter-1)*" "), (counter*'*')+'*'+(counter*'*'))
for y in range(0, trunk):
    print((((round(finalStars/2))-(round(trunk/2)))*" "), (trunk+1)*"*")
