#4. Python Program to Find the Second Largest Number in a List Using Bubble Sort

def bubbleSort(li):
    for i in range(1,len(li)):
        for j in range(0,len(li)-1):
            if(li[j] > li[j + 1]):
                li[j],li[j + 1] = li[j + 1],li[j]
                #print(li)    #How we can sort the li
                
    return li
    
li = [60 ,50, 40, 30, 20, 10]

print("List before sort : ",li)
li = bubbleSort(li)        
print("List after sort : ",li)  
print("Second Largest Number : ",li[-2])      
