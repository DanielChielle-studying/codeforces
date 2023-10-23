n, m = map(int, input().split())
clicks = 0

while m > n:
    if m % 2 == 0:
        m //= 2
        clicks += 1
    else:
        m += 1
        clicks += 1
        
clicks += abs(n - m)
print(clicks)