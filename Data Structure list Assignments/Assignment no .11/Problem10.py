#10. Write a program to print list after removing even numbers.

li = [1,2,3,4,5,6,7,8,9,10]
list = []

for i in li:
    if i% 2 != 0:
        list.append(i)
        
print("List after removing even numbers : ",list)        