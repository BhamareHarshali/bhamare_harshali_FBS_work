#3. Convert distant given in feet and inches into meter and centimeter.

#give input as feet and inches .
feet = int(input("Enter feet : "))   #30.48 cm
inches = int(input("Enter inches :")) #2.54 cm

#convert into total_cm     //    (feet * 30.48) + (inches * 2.5)
total_cm = (feet * 30.48) + (inches * 2.5)

#formula 
meter =(total_cm // 100)
centimeter = (total_cm % 100)

#Display output 
print(f'Distance = {meter} meter and {centimeter} centimeter .')