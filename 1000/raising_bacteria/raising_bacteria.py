n_bacterias = int(input())
b_bacteria = bin(n_bacterias)

n_ones = 0

for n in b_bacteria:
    if n == "1":
        n_ones+=1

print(n_ones)