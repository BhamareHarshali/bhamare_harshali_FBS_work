#10. Write a program to remove all occurrences of a given element in the list.

li = [10 ,20 ,30 ,40 ,50,20 ,20]

num = int(input("Enter element to remove: "))

list=[]
for i in li:
    if i != num:
        list.append(i)

print("Original list:", li)
print("List after removing", num, ":", list)        