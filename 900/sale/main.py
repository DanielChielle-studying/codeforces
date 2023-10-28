n, m = map(int, input().split())
tvs = sorted(list(map(int, input().split())))

sum_momey = 0

for i in range(m):
    if tvs[i] <= 0:
        sum_momey += abs(tvs[i])
    else:
        break

print(sum_momey)