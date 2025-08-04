#6. Write a program to calculate profit or loss.

c_p = float(input("Enter the cost price: "))
s_p = float(input("Enter the selling price: "))

#Formula sellping price - cost price //profit
if(s_p - c_p):
    print("Profit.")
#Formula cost_price - selling_price  // loss    
elif (c_p - s_p):
    print("Loss")    
else:
    print("No profit and No loss.")    