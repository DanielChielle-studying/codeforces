n = int(input())

for i in range(n):
    t = int(input())
    
    while t % 2 == 0:
        t = t / 2
    
    print("NO" if t == 1 else "YES")