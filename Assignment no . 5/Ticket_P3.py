#3. Accept no. of passengers from user and per ticket cost. 
# Then accept age of each passenger and then calculate total amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

num = int (input("Enter number of passengers: "))
ticket = float (input("Enter cost per ticket: "))

total_fare = 0

for i in range(1,num + 1):
    age = int(input("Enter age of passenger {i}: "))
    
    if age <12:
        fare = ticket * 0.7
    elif age > 59:
        fare = ticket * 0.5
    else:
        fare = ticket
        
    print(f"Fare for passenger {i} = {fare}.")
    total_fare += fare
    
print(f"Total fare for all passengers = {total_fare}.")                
          
    
        