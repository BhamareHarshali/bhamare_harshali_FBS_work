#4. Write a program to calculate the total cost of painting. The interior of building with fourequal sized walls.

height = int(input("Enter height of the wall: "))
width = int(input("Enter width of the wall: "))
cost_per_sq_meter = int(input("Enter cost of painting per square meter: "))

# Total area of 4 equal walls
area = 4 * height * width

# Total cost of painting
total_cost = area * cost_per_sq_meter

# Output the result
print("Total cost of painting the interior walls is: ", round(total_cost))

