a, b = map(int, input().split())
hours = a

while a >= b:
    candles = a // b
    hours += candles
    a = candles + (a % b)

print(hours)

