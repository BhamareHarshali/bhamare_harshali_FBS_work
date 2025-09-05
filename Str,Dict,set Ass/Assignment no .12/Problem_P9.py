#9. Python Program to Calculate the Number of Words and the Number of
#Characters Present in a String

str = "Python is easy to learn"

char_count = 0
for char in str:
    char_count += 1

words = str.split()    
word_count = 0
for  char in words:
    word_count += 1
    
print("String :",str)
print("total Charchters :",char_count)        
print("total Words :",word_count)        