#3. Create a class MedicalStudent inherited from Student with following:

#i. Data members :Specialization
#ii. MarksOfInternship
#b. Add the following methods :
#i. Parameterized constructor
#ii. Display
#iii. Accept
#iv. override Method CalculateRank
#v. Override __str__ Method



from Student import Student
class MedicalStudent(Student):
    def __init__(self, S_Id="", Name="", Age="", percentage="",Specialization="",MarksOfInternship=""):
        super().__init__(S_Id, Name, Age, percentage)
        self.S = Specialization
        self.M_I = MarksOfInternship 
        
    def DisplayData(self):
        super().DisplayData()
        print(f"Specialization: {self.S} \n MarksOfInternship: {self.M_I}")
        
    def accept(self):
        super().accept()  
        self.S = (input ("Enter Specialization:"))  
        self.M_I = float (input("Enter MarksOfInternship:"))
         
    def CalculateRank(self):
        super().CalculateRank() 
        result = (float(self.per *0.7) + float(self.M_I * 0.3))
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
        return (f"Branch: {self.S}\n"
                f"Internal Marks: {self.M_I}\n"
                f"Rank: {self.CalculateRank()}")   
s1 = MedicalStudent(Student)
s1.accept()
print("\nUsing __str__ method:")
s1.DisplayData()        