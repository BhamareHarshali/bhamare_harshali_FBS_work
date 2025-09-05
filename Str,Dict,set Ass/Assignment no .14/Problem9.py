#9. Write a Python program to find all the unique combinations of 3
#numbers from a given list of numbers, adding up to a target number.

n = [ 1,2,3,5,6,7,8,9]
target = 10
adding=set()

for i in range(len(n)):
    for j in range(i+1,len(n)):
        for k in range(j+1,len(n)):
            if n[i] + n[j] +n[k] == target:
                adding.add(tuple(sorted([n[i],n[j],n[k]])))
                
for t in adding:
    print(t)                