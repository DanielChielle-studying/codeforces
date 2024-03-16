n, t = map(int, input().split())
cells = list(map(int, input().split()))

current_cell = 1

while current_cell < t:
    current_cell += cells[current_cell - 1]

    if current_cell == t:
        print("YES")
        break
    if current_cell > t:
        print("NO")
        break

