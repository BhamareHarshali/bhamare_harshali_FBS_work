#6. Python Program to Find the Union of two Lists

li1 = [1,2,3,4,5]
li2 = [4,5,6,7,8]

union_list = list(set(li1) | set(li2))

print("Oringal list : ",li1 ,li2)
print("Union of the lsits : ",union_list)