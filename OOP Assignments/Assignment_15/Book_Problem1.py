#1. Create a class Book with members as bid,bname,price and author.Add following methods:
#a. Constructor (Support both parameterized and parameterless)
#b. Destructor
#c. ShowBook

class Book:
    def __init__(self,b_id="",b_nm="",b_Author="",b_price=" "):
        self.bid = b_id
        self.bnm = b_nm
        self.b_au = b_Author
        self.p = b_price
    
    def showBook(self):
        print("\nB_ID:",self.bid) 
        print("Book Name:",self.bnm)  
        print("Price:",self.b_au) 
        print("Author:",self.p)
    def __del__(self):
        print(f"Destructor called {self.bnm}:({self.bid}) Deleted.")  
        
book1 = Book(101,"The C++ Programming Language", 650, "Bjarne Stroustrup")
book1.showBook()  

book2 = Book(102, "Introduction to Python", 700, "Guido van Rossum")       
book2.showBook()        
        