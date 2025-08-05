#5. A man goes for shopping. He buys 5 P. Accept the price of all P and display the total bill after adding 18% GST

P1 = float(input("Enter price of product 1: "))
P2 = float(input("Enter price of product 2: "))
P3 = float(input("Enter price of product 3: "))
P4 = float(input("Enter price of product 4: "))
P5 = float(input("Enter price of product 5: "))

total = P1 + P2 + P3 + P4 + P5 

gst = total * 0.18

final_amount =total + gst

print(f'Total  Gst:{gst}')
print(f'Final bill amount : {final_amount}')