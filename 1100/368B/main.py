n, m = map(int, input().split())
a = list(map(int, input().split()))

count = {}
result = []

for i in range(n - 1, -1, -1):
    count[a[i]] = 1
    result.append(len(count))

result.reverse()

for _ in range(m):
    l = int(input())    
    print(result[l-1])
