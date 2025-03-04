#   Enter a number: 4
#   ****
#   ***
#   **
#   *
stal = int(input("Enter a number for rows of the triangle: "))
for x in range(stal+1, 0, -1):
    print(x*'*')
