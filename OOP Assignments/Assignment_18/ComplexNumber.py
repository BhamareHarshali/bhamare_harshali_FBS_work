#1. Create a class Complex Number with data members as real and imag and add
#following methods :
#a. Constructor
#b. Destructor
#c. Overload +,- operator

class ComplexNumber:
    def __init__(self , real =0, img=0):
        self.real =  real
        self.img = img 
        
    def __del__(self):
        print(f'Complex Number {self} destroyed. ')
    
    def __add__(self,other):
        return ComplexNumber(self.real + other.real, self.img + other.img) 
    
    def __sub__(self,other):
        return ComplexNumber(self.real - other.real, self.img - other.img)
     
    def __str__(self):
        return (f'{self.real} + {self.img}i' if self.img >= 0 else f"{self.real} - {-self.img}i")
        
        
c1 = ComplexNumber(3,4)
c2 = ComplexNumber(1,-2) 

c3 = c1 + c2 
c4 = c1 - c2    

print("c1 =", c1)
print("c2 =", c2)
print("c1 + c2 =", c3)
print("c1 - c2 =", c4)