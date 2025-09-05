#7. Python Program to Remove the Given Key from a Dictionary

d = {1:"C" , 2: "Python" , 3:"C++" , 4 :"Core Python"}

key = int(input("Enter the key to remove:"))

if key in d:
    d.pop(key)
    print(d)
else:
    print("Key not found in dictionary!")    
    