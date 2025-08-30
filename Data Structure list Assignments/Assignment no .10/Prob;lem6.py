#6. Write a program to remove duplicates from the list.

li = [10 ,20 ,30 ,40 ,20 ,10 ,50]

list = []

#Using membership opreator
for i in li:
    if i not in list:
        list.append(i)
print("List after removing duplicates:", list)        