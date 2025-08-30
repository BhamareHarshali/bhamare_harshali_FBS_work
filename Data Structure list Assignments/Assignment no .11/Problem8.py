#8. Print 1 to 100 in snakes and ladder pattern.

n = 1
for i in range(10):
    line = []
    for j in range(10):
        line.append(n)
        n += 1
        
    if i%2 == 0:
        line.reverse()
    print(line)        