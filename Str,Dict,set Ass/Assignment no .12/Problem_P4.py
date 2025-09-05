#4. Python Program to Form a New String where the First Character and the Last Character have been Exchanged

str = "Harshali"


if len(str) <= 1:
    new_str = str
    
else:
    new_str = str[-1] + str[1 : -1] + str[0]   
    
print("Modified String : ",new_str)     