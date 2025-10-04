#2. Create a class Product with members as pid,pname,price and quantity .Add
#following methods:
#e. Constructor (Support both parameterized and parameterless)
#f. Destructor
#g. ShowBook
#h. Add static member discount.
#i. Provide methods for applying discount on price of product.

class Product:
    count = 0
    def __init__(self,p_id=0,p_nm="",b_price="",p_Quantity=" "):
        self.p_id = p_id
        self.p_name = p_nm
        self.p_price = b_price
        self.p_Quantity = p_Quantity
        
        Product.count +=1 
        
    def showProduct(self):
        print("\nP_ID:",self.p_id) 
        print("Product Name:",self.p_name)  
        print("Product Price:",self.p_price) 
        print("Product Quantity:",self.p_Quantity)
      
    def __del__(self):
        print(f"Destructor called {self.p_name}:({self.p_id}) Deleted.") 
        
    @staticmethod
    def showCount():
        print(f"Total Product objects created: {Product.count}")     
print("_________________________________________")        
Prod1 = Product(201, "Sumsung", "55,0000", 5)
Prod1.showProduct()  
print("_________________________________________")
Prod2 = Product(202, "Dell", "62,0000", 10)       
Prod2.showProduct()     
print("_________________________________________")
Product.showCount()
print("_________________________________________")