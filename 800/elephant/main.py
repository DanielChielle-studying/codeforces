x = int(input())

steps = [1, 2, 3, 4, 5]
i = 4
count = 0

while x != 0:
    if x - steps[i] >= 0:
        x -= steps[i]
        count += 1
    else:
        i -= 1

print(count)