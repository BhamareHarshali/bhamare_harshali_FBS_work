#6. Python Program to Multiply All the Items in a Dictionary

d = {1:2 , 2:3 , 3:4 , 4:5}

print(d)

# Multiply all values
res =1
for value in d.values():
    res *= value
    
print("Multiplication of all items: ",res)    