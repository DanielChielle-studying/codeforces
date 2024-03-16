n_shops = int(input())
shops = [int(num) for num in input().split()]
days = int(input())

vetor = [0]*(100001)

for s in shops:
    vetor[s] += 1

i = 1

while i < len(vetor):
    vetor[i] += vetor[i-1]
    i+=1

for _ in range(days):
    coin = int(input())

    if coin >= len(vetor):
        print(vetor[-1])
    else:
        print(vetor[coin])