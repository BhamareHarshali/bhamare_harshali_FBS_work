#8. Python Program to Remove the Characters of Odd Index Values in a String

str = "Python"
new_str=" "

for i in range(len(str)):
    if i % 2== 0:     # keep only even index characters
        new_str += str[i]
        
print("Orignal String: ",str)
print("Modified String: ",new_str)        
