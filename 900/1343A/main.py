def find_x(n):
    x = 3
    while n % x != 0:
        x = (x*2) + 1

    return int(n/x)

t = int(input())

for _ in range(t):
    n = int(input())
    x = find_x(n)
    print(x)

