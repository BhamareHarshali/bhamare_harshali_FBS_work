#1. Python Program to Replace all Occurrences of ‘a’ with $ in a String

str = "apple are amazing"

new_str = " "
for char in str:
    if char == "a":
        new_str += "$"
        
    else:
        new_str += char

print("Modified String: ",new_str)        
            
