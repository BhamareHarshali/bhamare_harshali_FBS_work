#2. Create a class Distance with data members as km,m and cm and add following methods :
#a. Constructor
#b. Destructor
#c. Overload +,- operator

class Distance:
    def __init__(self, km=0, m=0, cm=0):       
        self.km = km
        self.m = m
        self.cm = cm
        
    def __del__(self):
        print(f"Distance {self} destroyed.")

    def _normalize(self):
        if self.cm >= 100:
            self.m += self.cm // 100
            self.cm = self.cm % 100

        if self.m >= 1000:
            self.km += self.m // 1000
            self.m = self.m % 1000

        if self.cm < 0 or self.m < 0 or self.km < 0:
            pass  # keeping it simple, no complex negative normalization here

    def __add__(self, other):
        return Distance(self.km + other.km,
                        self.m + other.m,
                        self.cm + other.cm)

    def __sub__(self, other):
        return Distance(self.km - other.km,
                        self.m - other.m,
                        self.cm - other.cm)

    def __str__(self):
        return f"{self.km} km {self.m} m {self.cm} cm"


# Example usage
d1 = Distance(2, 850, 90)  
d2 = Distance(1, 300, 50) 

d3 = d1 + d2
d4 = d1 - d2

print("Add:", d3)
print("Sub:", d4)
