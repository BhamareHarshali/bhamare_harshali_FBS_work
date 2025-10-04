#3. Create a class Shirt with members as sid,sname,type(formal etc), price and
#size(small,large etc) .Add following methods:
#g. Constructor (Support both parameterized and parameterless)
#h. Destructor
#i. ShowBook

class Product:
    def __init__(self,s_id=0,s_nm="",type="",price=" ",size=""):
        self.s_id = s_id
        self.s_name = s_nm
        self.s_price = price
        self.s_type = type
        self.s_size = size
    
    def showShrit(self):
        print("\ns_ID:",self.s_id) 
        print("Shrit Name:",self.s_name)  
        print("Shrit Price:",self.s_price) 
        print("Shrit Type:",self.s_type) 
        print("Shrit size:",self.s_size)
      
    def __del__(self):
        print(f"Destructor called {self.s_name}:({self.s_id}) Deleted.")  
        
Prod1 = Product(301, "Formal Shrit", "Formal", 1200,"L")
Prod1.showShrit()  

Prod2 = Product(302, "Casual T-Shirt", "Casual", 800, "M")       
Prod2.showShrit() 