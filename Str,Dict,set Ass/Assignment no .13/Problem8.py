#8. Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

d ="Python  is easy to learn , Python is fun "

words =d.split()
freq = {}

for word in words:
    freq[word] = freq.get(word ,0)+1
    
print("Word frequence :",freq)    