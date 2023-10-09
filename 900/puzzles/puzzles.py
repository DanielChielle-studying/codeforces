n, m = map(int, input().split())
puzzles = sorted([int(x) for x in input().split()])

A_minus_B = puzzles[n-1] - puzzles[0]

for i, p in enumerate(puzzles[:len(puzzles) - n+1]):
    values = puzzles[i:i+n]
    difference = max(values) - min(values)
    A_minus_B = difference if difference < A_minus_B else A_minus_B

print(A_minus_B)