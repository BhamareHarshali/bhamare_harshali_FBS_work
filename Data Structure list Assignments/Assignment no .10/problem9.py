#9. Write a program of having n number of elements in the list and find out even and odd elements in that list and then create two separate lists which will have
#even elements and other will have odd elements.

n = int(input("Enter number of elements :"))

li = []
for i in range(n):
    num = int(input("Enter Element: "))
    li.append(num)
    
even_list = []
odd_list = []    

for i in li:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

        
print("Original list:",li)
print("Even element list: ",even_list) 
print("Odd elements list: ",odd_list)           