#1. Create a class Student with following
#a. data members :
#i. StudentId
#ii. Name
#iii. Age
#iv. Percentage
#b. Add the following methods :
#i. Parameterized constructor
#ii. Display
#iii. Accept
#iv. Method CalculateRank
#v. Override __str__ Method


class Student:
      # Constructor: can be used with or without arguments
    def __init__(self,S_Id="",Name="",Age="",percentage=""):
        self.std_id = S_Id
        self.nm = Name
        self.age =Age
        self.per = percentage
         
    def accept(self):
        self.std_id = int(input("Enter S_id: "))       
        self.nm= (input("Enter Student Name: "))
        self.age= int(input("Enter Student Age: "))
        self.per= float(input("Enter Student Percentage: "))
        
    def CalculateRank(self):
        if self.per is None:
            return "No Data."
        if self.per >= 85:
            return "Distinction."
        if self.per >= 78:
            return "First Class."
        if self.per >= 65:
            return "Second Class."
        if self.per >= 40:
            return "Pass."
        else:
            return "Fail."
       
    def DisplayData(self):
        print("Student_id:",self.std_id,
              "\nName:",self.nm,
              "\nAge:",self.age,
              "\nPercentage:",self.per,
              "\nRank:",self.CalculateRank())
            
    def __str__(self):
        return (f"Student_id: {self.std_id}\n"
            f"Name: {self.nm}\n"
            f"Age: {self.age}\n"
            f"Percentage: {self.per}\n"
            f"Rank: {self.CalculateRank()}")
        
        
#s1 = Student()  # Create empty student object
#s1.accept()    # Take input from user
#print("\nUsing __str__ method:")
#s1.DisplayData()   # Display using method




       
      
             
    