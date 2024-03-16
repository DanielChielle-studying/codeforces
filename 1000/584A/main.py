n, t = map(int, input().split())

num = 10 ** (n-1)

while len(str(num)) == n:
    if num % t == 0:
        print(num)
        break
    num += 1
else:
    print(-1)


    