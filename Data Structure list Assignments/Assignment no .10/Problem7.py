#7. Write a program to create a new list from existing list which contains cube of each number of list.

li = [1,2,3,4,5]

cube_list = []
for i in li:
    cube_list.append(i ** 3)
    
print(f"Orignal list: {li}")    
print(f"Cube list: {cube_list}")    