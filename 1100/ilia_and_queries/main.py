s = input()
n = int(input())
vector = [0]*len(s)

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        vector[i] = vector[i-1] + 1
    else:
        vector[i] = vector[i-1]

for i in range(n):
    a, b = map(int, input().split())
    print(vector[b-1] - vector[a-1])

