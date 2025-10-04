#3. Create a class Shirt with members as sid,sname,type(formal etc), price and
#size(small,large etc) .Add following methods:
#j. Constructor (Support both parameterized and parameterless)
#k. Destructor
#l. ShowBook
#m. For each size of shirt price should change by 10%.
#(eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and
#xlarge=1300) Use static concept.

class Shrit:
    count= 0
    def __init__(self,s_id=0,s_nm="",type="",price=" ",size=""):
        self.s_id = s_id
        self.s_name = s_nm
        self.s_price = price
        self.s_type = type
        self.s_size = size
        Shrit.count += 1
    def showShrit(self):
        print("\ns_ID:",self.s_id) 
        print("Shrit Name:",self.s_name)  
        print("Shrit Price:",self.s_price) 
        print("Shrit Type:",self.s_type) 
        print("Shrit size:",self.s_size)
      
    def __del__(self):
        print(f"Destructor called {self.s_name}:({self.s_id}) Deleted.")  
    
    @staticmethod
    def showCount():
        print(f"Total Shrit objects created: {Shrit.count}")     
print("_________________________________________")    
s1 = Shrit(301, "Formal Shrit", "Formal", 1200,"L")
s1.showShrit()  
print("_________________________________________")
s2 = Shrit(302, "Casual T-Shirt", "Casual", 800, "M")    
print("_________________________________________")   
s2.showShrit() 
print("_________________________________________")