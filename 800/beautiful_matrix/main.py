for i in range(5):
    m = list(map(int, input().split()))
    if 1 in m:
        dist = abs(2 - i) + abs(2 - m.index(1))

print(dist)