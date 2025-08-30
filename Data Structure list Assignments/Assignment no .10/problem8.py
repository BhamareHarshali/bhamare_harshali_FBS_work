#8. Write a program to create a duplicate of an existing list. It should not point to same list.

li = [10 ,20 ,30 ,40 ,50]

dup_list=[]
for i in li:
    dup_list.append(i)

 
print(f"Orignal list {li}.")
print(f"duplicate list {dup_list}.")