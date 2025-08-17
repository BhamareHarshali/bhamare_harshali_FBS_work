#          1 
#        2 3 2
#      3 4 5 4 3
#    4 5 6 7 6 5 4
#  5 6 7 8 9 8 7 6 5



# Top half
for i in range(1, 6):
    for j in range(1, 7 - i):
        print(" ", end=" ")

    # increasing numbers
    num = i
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1

    # decreasing numbers
    num -= 2
    for j in range(1, i):
        print(num, end=" ")
        num -= 1

    print()
