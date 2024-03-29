def min_party_groups(n):
  managers = []
  chain_lengths = [0] * (n + 1)

  for _ in range(n):
    managers.append(int(input()))
    
  for i in range(1, n + 1):
    current = i
    chain = 0
    while current != -1:
      chain += 1
      current = managers[current - 1] 
    chain_lengths[i] = chain

  max_chain = max(chain_lengths)
  return max_chain

n = int(input())
min_groups = min_party_groups(n)

print(min_groups)
