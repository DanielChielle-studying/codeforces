n_laptops =  int(input())
laptops = []

for i in range(n_laptops):
    p, q = map(int, input().split())
    laptops.append((p, q))

laptops.sort()

for i in range(1, n_laptops):
    if laptops[i][1] < laptops[i-1][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")
