#6. Python Program to Take in a String and Replace Every Blank Space with Hyphen

str = "Python easy to learn"
new_str = " "

for char in str:
    if char == " ":
        new_str += "-"
    else:
        new_str += char
            
print("Orignal String:",str)
print("Hypen String :",new_str)