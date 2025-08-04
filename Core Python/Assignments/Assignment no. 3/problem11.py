#11. Accept age of five people and also per person ticket amount 
# then calculate total amount to ticket to travel for all of them based on following condition :
#a. Children below 12 = 30% discount
#b. Senior citizen (above 59) = 50% discount
#c. Others need to pay full.

age1= int(input("Enter age of person 1: "))
age2= int(input("Enter age of person 2: "))
age3= int(input("Enter age of person 3: "))
age4= int(input("Enter age of person 4: "))
age5= int(input("Enter age of person 5: "))

ticke_amt = int(input("Enter the ticket amount :"))
#person 1
if(age1 < 12):
    dis_amt = ticke_amt * 0.3  #30%
    amt1 = ticke_amt - dis_amt
elif(age1 > 59):
    dis_amt = ticke_amt * 0.5  #50% 
    amt1 = ticke_amt - dis_amt
else:
    amt1 =ticke_amt  
    
#person 2
if(age2 < 12):
    dis_amt = ticke_amt * 0.3 
    amt2 = ticke_amt - dis_amt
elif(age2 > 59 ):
    dis_amt = ticke_amt *0.5
    amt2 = ticke_amt - dis_amt
else:
    amt2 = ticke_amt
    
#person 3

if(age3 < 12):
    dis_amt = ticke_amt * 0.3
    amt3 = ticke_amt - dis_amt 
elif(age3 > 59):
    dis_amt = ticke_amt * 0.5
    amt3 = ticke_amt - dis_amt
else:
    amt3 = ticke_amt 
    
# person 4  

if(age4 < 12):
    dis_amt = ticke_amt * 0.3
    amt4 = ticke_amt - dis_amt
elif(age4 > 59):
    dis_amt = ticke_amt * 0.5 
    amt4 = ticke_amt - dis_amt
else:
    amt4 = ticke_amt 
    
#person 5

if(age5 < 12):
    dis_amt = ticke_amt * 0.3
    amt5 = ticke_amt - dis_amt
elif(age5 > 59):
    dis_amt = ticke_amt * 0.5
    amt5 = ticke_amt - dis_amt
else: 
    amt5 = ticke_amt  
    
total_amt = amt1 + amt2 + amt3 + amt4 + amt5
print(total_amt)
                                   