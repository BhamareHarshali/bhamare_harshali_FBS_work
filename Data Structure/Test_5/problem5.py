#Write a Python program to find union of two lists without using set aoncept

li1 = [1,2,3,4,5]
li2 = [4,5,6,7,8]

union_list = []
for i in li1:
    if i not in union_list:
        union_list.append(i)
for j in li1:
    if j not in union_list:
        union_list.append(j) 
        
print("Union of two lists:", union_list)              