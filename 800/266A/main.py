n = int(input())
stones = input()

count = 0
current = stones[0]

for s in stones[1:]:
    if s == current:
        count += 1
    current = s

print(count)
