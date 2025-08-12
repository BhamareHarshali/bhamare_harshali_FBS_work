#5. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount. (Use looping to optimize the problem)

amount = int(input("Enter the amount : "))
notes =[2000 , 500, 200, 100, 50, 20, 10,5 ,2,1]
total = 0

for note in notes:
    total+= amount // note
    amount %= note
    
print("Minimum number of notes: ",total)    