#5. WAP to calculate selling price of book based on cost price and discount.

cost_price = float(input("Enter the cost prime of book :"))
discount = float(input("Enter the discount : "))

#discount_amount = (cost_price * discount) / 100
#formula of selling price:-                //    (sp = cp - dis * cp /100) 
selling_price = cost_price - discount * cost_price /100

#Display output
print(f'Selling price of book base on cost and discount is : {selling_price} .')


