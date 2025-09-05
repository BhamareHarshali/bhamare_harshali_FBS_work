#3. Python Program to Check if a Given Key Exists in a Dictionary or Not

d1 = { 1 :"C", 2 :"Python",3 :"C++" , 4:"Java"}

key = int(input("Enter key to check : "))
if key in d1:
    print(f"Yes ,key {key} exists with value '{d1[key]}'")
else:    
    print(f"No ,key {key} does not exists")
    