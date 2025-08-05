#3. A farmer has a field which is half in circle share and rest rectangle. 
#He needs to do fencing for entire field using barbed wire 5 times. 
#Circular section has radius 20m and rectangle length is 50 m and breadth is 40m.
# If cost of barbed wire is 35Rs/m then calculate the total cost of fencing the field.


# Given values
radius = 20                  
length = 50                  
breadth = 40                 
layers = 5                   
cost_per_meter = 35          

# Perimeter of rectangle 
rectangle_fencing = length + breadth 

# Perimeter of half-circle = π * r
half_circle_fencing = 3.14 * radius      

# Total fencing length (single layer)
total_length = rectangle_fencing + half_circle_fencing

# Multiply by 5 layers
total_wire_length = total_length * layers

# Total cost
total_cost = total_wire_length * cost_per_meter

print("Total cost of fencing the field is: ₹", round(total_cost))
