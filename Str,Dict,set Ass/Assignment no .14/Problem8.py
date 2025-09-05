#8. Write a Python program to find all the anagrams and group them
#together from a given list of strings.

words = ["eat","ate","tan","bat"]

anagram = {}

for i in words:
    key = "".join(sorted(i))
    anagram.setdefault(key,[]).append(i)
    
for j in anagram.values():
    print(j)    