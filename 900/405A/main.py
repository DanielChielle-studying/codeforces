n = int(input())
columns = [int(num) for num in input().split()]
sorted_col = sorted(columns)
for n in sorted_col:
    print(n, end=" ")

print()

