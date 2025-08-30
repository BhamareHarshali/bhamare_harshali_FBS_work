#2. Write a program to find maximum and minimum element in a list.

li = [20, 40, 84, 5, 10]

# assume first element is maximum and minimum
maximum = li[0]
minimum = li[0]

for num in li:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print(f"Maximum element {maximum}.")
print(f"Minimum element {minimum}.")
