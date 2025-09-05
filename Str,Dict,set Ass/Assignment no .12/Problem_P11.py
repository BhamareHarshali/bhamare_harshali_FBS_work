#11. Python Program to replace every blank space with hyphen in a string.

str = "Python ia easy to leran ."

new_str =" "

for char in str:
    if char == " ":
        new_str += "-"
        
    else:
        new_str += char
        
print("Original String:",str)
print("Modified String :",new_str)            