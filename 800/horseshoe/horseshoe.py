horseshoes = input().split()

count = {}

for hs in horseshoes:
    if hs in count:
        count[hs] += 1
    else:
        count[hs] = 1 

same_hs = 0

for value in count.values():
    if value > 1:
        same_hs += value - 1
    
print(same_hs)
