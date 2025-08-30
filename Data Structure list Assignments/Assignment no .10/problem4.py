#4. Write a program to reverse the list.

li = [10 ,20 ,30 ,40 ,50]

start = 0 
end = len(li) -1

while start < end:
    li[start] , li[end] = li[end] , li[start]
    start += 1
    end -= 1

print(f'Reversed list is {li}')