n = int(input())
numbers = list(map(int, input().split()))

even = 0
odd = 0
last_even = 0
last_odd = 0

for i in range(n):
    if numbers[i] % 2 == 0:
        even += 1
        last_even = i
    else:
        odd += 1
        last_odd = i

print(last_even + 1 if even == 1 else last_odd + 1)

