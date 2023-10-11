n, m = map(int, input().split())

count = 0
i = 0

while True:
    if n - i == 0:
        break
    if m - i == 0:
        break

    i += 1
    count += 1

print("Malvika") if count % 2 == 0 else print("Akshat")
    