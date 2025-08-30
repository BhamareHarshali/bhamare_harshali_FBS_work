#1. Python Program to Put Even and Odd elements of a List into two Different Lists

li = [1,2,3,4,5,6,7,8,9,10]

even_li = []
odd_li=[]

for i in li:
    if i % 2 == 0:
        even_li.append(i)
    else:
        odd_li.append(i)

print(f'Orignal list : {li}')
print(f'Even number list : {even_li}')
print(f'Odd number list : {odd_li}')
            