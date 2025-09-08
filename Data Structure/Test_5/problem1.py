#1.A list contains the denominational as follows:
#D = [2000, 500, 200, 100, 50, 20, 10, 5]
#Accept an amount from the user and calculate how many minimum number of notes will be needed for that amount.

D = [2000, 500, 200, 100, 50, 20,10,5]

amount = int(input("Enter the amount: "))

print("Amount: ",amount)
print("Note required: ")

for note in D:
    count = amount // note
    amount = amount % note
    print(f"{note} X {count}")