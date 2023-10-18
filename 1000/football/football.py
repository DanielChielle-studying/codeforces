n = int(input())
score = {}

for x in range(n):
    goal = input()

    if goal not in score:
        score[goal] = 1
    else:
        score[goal] += 1

max_score = max(score, key=score.get)
print(max_score)
