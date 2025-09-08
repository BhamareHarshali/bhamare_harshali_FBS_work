#There is a list with some integer values.
# Create a new dictionary using list in such a way that key is number and value is frequency of occurrence of that number in list
#{1,3,4,1,2,3,6,7,,1,2,4}
#{1:3,3:2,2:2} 

li = [1,3,4,1,2,3,6,7,1,2,4]
freq = {}

for num in li:
    if num in freq:
        freq[num]+=1
    else:
        freq[num]=1
print(freq)            
    
