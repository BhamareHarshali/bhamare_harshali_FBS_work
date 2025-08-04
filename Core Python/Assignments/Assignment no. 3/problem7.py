#7. Write a program to check if user has entered correct userid and password.

import random

Username = "Harshali"
password = "pass@123"

Username =(input("Username: "))
password =(input("password: "))

if(Username == "Harshali" and password == "pass@123"):
    print("User & pass is correct , So it is successfuly login")
else:
    print("user & pass is worong ,  So it is unsuccessful to login")            
