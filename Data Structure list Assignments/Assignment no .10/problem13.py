#13 . Write a program to print list after removing even numbers.

li = [1,2,3,4,5,6,7,8,9,10]

list=[]
for num in li:
    if num % 2!= 0:
        list.append(num)

print("Original List:", li)
print("List after removing even numbers:", list)        