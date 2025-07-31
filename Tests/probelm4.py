#4. Calculate the cost of painting the following building’s walls (both interior and exterior).
# You need to accept area (one wall) and cost of both interior and exterior wall.
#(Note: 
# 1. Below diagram is of two joint rooms.
# 2. It is upper view of building.)

side = int(input("Enter side of room : "))
interior = int(input("Enter the cost of interior painting is : "))
exterior =  int(input("t Enter the cost of the exterior painting is : "))

total_area = 4 * side * side

total_cost = total_area *interior * total_area * exterior 

print(f'Total cost of painting 2 room Rs : {total_cost}')

