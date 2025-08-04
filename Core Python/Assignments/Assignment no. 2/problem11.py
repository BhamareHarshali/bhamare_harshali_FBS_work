#11. Write a program to accept an integer amount from user and tell minimum number of notes needed for representing that amount.

amt = int(input("Enter the amount :"))
temp = amt

two_thousand = temp // 2000
temp = temp % 2000

five_Hundred = temp // 500
temp = temp % 500

two_hundred = temp // 200
temp = temp % 200

hundred = temp // 100
temp = temp % 100

fifty = temp // 50 
temp = temp % 50

twenty = temp // 20
temp = temp % 20

ten = temp // 10
temp = temp % 10 

total_notes = two_thousand + five_Hundred + two_hundred + hundred + fifty + twenty + ten 

print (f'Total Notes : { total_notes}')


