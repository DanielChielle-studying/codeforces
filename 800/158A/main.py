number, mim_score = input().split()
position = int(mim_score)
scores = [int(score) for score in input().split()]

mim_score = scores[position-1]
n_advance = 0

for s in scores:
    if s >= mim_score and s > 0:
        n_advance +=1

print(n_advance)