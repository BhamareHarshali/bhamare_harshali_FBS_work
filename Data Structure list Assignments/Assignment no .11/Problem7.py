#7. Python Program to Find the Intersection of Two Lists

li1 = [1,2,3,4,5]
li2 = [3,4,5,8,9,10]

intersection_list = list(set(li1) & set(li2))

print("Intersection of two lists :",intersection_list)