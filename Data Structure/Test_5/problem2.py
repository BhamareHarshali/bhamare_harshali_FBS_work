#A teacher came to class with a large box that has several coins. Each coin has a number printed on it.
#Before coming to class, she ensured that all the numbers occur an Even number of times.
#However, while coming to the class, one coin fell down and got lost.
# She wants to find out the number on the missing coin.
#Inputs: The original number of coins and the actual number on each of the coins, separated by spaces.

#Output: The number on the missing coin.
#Sample Input:8 5 7 2 7 5 2 5
#Sample Output: 5

# Input the total number of coins
n = int(input("Enter total number of coins: "))

# Input the numbers on the coins as space-separated values
coins = list(map(int, input("Enter the coins numbers: ").split()))

# Find the coin that occurs odd number of times (the missing one)
for coin in coins:
    if coins.count(coin) % 2 != 0:
        print("The missing coin number is:", coin)
        break  # Exit after finding the missing coin
