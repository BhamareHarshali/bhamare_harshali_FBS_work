#2. Create a derived class from Student as EnggStudent with :
#a. Data members as :
#i. Branch
#ii. InternalMarks
#b. Add the following methods :
#i. Parameterized constructor
#ii. Display
#iii. Accept
#iv. override Method CalculateRank
#v. Override __str__ Method

from Student import Student
class EnggStudent(Student):
    def __init__(self, S_Id="", Name="", Age="", percentage="",branch="",internal_marks=""):
        super().__init__(S_Id, Name, Age, percentage)
        self.Branch = branch
        self.Internal_marks = internal_marks    
        
    def DisplayData(self):
        super().DisplayData()
        print("Branch:",self.Branch) 
        print("Internal_Marks:",self.Internal_marks)
        
    def accept(self):
        super().accept()    
        self.Branch = (input("Enter Branch:"))
        self.Internal_marks = float(input("Enter Internal Marks:"))
    
    def CalculateRank(self):
        result = (float(self.per) + float(self.Internal_marks)) /2
        if result is None:
            return "No Data."
        if result >= 85:
            return "Distinction."
        if result >= 78:
            return "First Class."
        if result >= 65:
            return "Second Class."
        if result >= 40:
            return "Pass."
        else:
            return "Fail."
       
        
    def __str__(self):
          return (f"Branch: {self.Branch}\n"
                f"Internal Marks: {self.Internal_marks}\n"
                f"Rank: {self.CalculateRank()}")
    
s1 = EnggStudent()
s1.accept()
print("\nUsing __str__ method:")
s1.DisplayData()


       
