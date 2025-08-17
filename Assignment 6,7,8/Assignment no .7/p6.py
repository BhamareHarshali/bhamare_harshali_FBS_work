for i in range(1, 6):
    for j in range(1, 6):
        if i == 1:               # first row → print 1 2 3 4 5
            print(j, end=" ")
        elif j == i or j == 5:   # diagonal (j==i) or last column (j==5)
            print(j, end=" ")
        else:                    # spaces in between
            print(" ", end=" ")
    print()
