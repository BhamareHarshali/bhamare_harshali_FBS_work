#5. Accept a number from user and check if this element is present in the list or not. Also tell how many times it is present in the list.

li = [10, 20 ,30 ,40 ,10 , 30]

num = int(input("Enter the number to search: "))
#count = 0
#for i in li:
#    if i == num:
#       count +=1 

if num in li:
    print(num , "is present in the list",li.count(num) , "times.")
    
else:
    print(num , "is not present in the list.")            
        