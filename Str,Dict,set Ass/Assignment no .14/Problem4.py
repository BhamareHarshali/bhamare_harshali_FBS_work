#4. Write a Python program that finds all pairs of elements in a list whose
#sum is equal to a given value.

li = [2,3,4,5,6,7,8,9,10]
value = 15

for i in range (len(li)):
    for j in range(i+1,len(li)):
        if  li[i]+li[j] == value: 
            print(li[i],"+",li[j],"=",value)

