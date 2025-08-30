#3. Python Program to Sort the List According to the Second Element in Sublist

def sort_by_second(sublist):
    return sublist[1]

li = [[1,3] , [4,1] , [2,5] ,[6,2]]

sorted_list = sorted(li ,key = lambda x : x[1])

print("Original List : ",li)
print("Sorted List (by second element):",sorted_list)