#             A  
#          A  B  C  
#       A  B  C  D  E  
#    A  B  C  D  E  F  G  
# A  B  C  D  E  F  G  H  I 



rows = 5

for i in range(1, rows + 1):
    # spaces before letters
    print("   " * (rows - i), end=" ")

    # print letters (A, B, C …)
    for j in range(1, 2 * i):
        print(chr(64 + j), end="  ")
    print()
