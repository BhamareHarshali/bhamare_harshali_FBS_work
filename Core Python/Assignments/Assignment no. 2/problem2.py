#2. Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

celsius = float(input("Enter the temperature in celsius : "))

#formula  (C/5 = (F-32)/9)
fahrenheit = (9/5) * celsius +32

#Display output
print(f'Temperature in fahrenheit :{fahrenheit} . ')