#14. Python Program to count the occurrences of ach word in a string.

str = "apple are amazing"

new_str = " "
for char in str:
    if char == "a":
        new_str += "ach"
    else:
        new_str += char

print("Modified String: ",new_str)        
                