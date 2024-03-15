number, position = [int(x) for x in input().split()]

if position <= (number+1)//2:
    n = 2 * position - 1
else:
    n = 2 * (position - (number+1) // 2)

print(abs(n))


