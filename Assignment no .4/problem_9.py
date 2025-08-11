#9. WAP to print all numbers in a range divisible by a given number.
start = int(input("Enter the start of the range :"))
end = int(input("Enter the end of the range: "))
divide = int(input("Enter the divide : "))

print(f"Number divisible by :{divide}. ")

for i in range (start,end+1):
    if i % divide == 0:
        print(i)