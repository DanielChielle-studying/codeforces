number_coins = int(input())
input_line = input()

input_numbers = input_line.split()

coins_value = [int(num) for num in input_numbers]
coins_sorted = sorted(coins_value, reverse=True)


coins_taken = 0
coin_sum = 0 
for index, coin in enumerate(coins_sorted):
    if coin_sum <= sum(coins_sorted[index:]):
        coin_sum+=coin
        coins_taken+=1

print(coins_taken)