 #1. Write a program to prompt user to enter userid and password.
 # If Id and password is incorrect give him chance to re-enter the credentials.
 # Let him try 3times. After that program to terminate.
 
User = "Harshali"
Pass = "Harshu@123"

chance = 3

while chance > 0:
    Userid = input("Enter the userid: ")
    Password = input("Enter the password: ")
    
    if Userid == User and Password == Pass :
        print("Login sucessfull !!")
        break
    else:
        chance -= 1
        if chance > 0:
            print(f"Incorrect credentials {chance} left.")
        else:
            print("To many fail attempts. Program to Terminate.")        