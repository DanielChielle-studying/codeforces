number = int(input())

answers = []
solver_ex = 0

for index in range(number):
    answers = p, v, t = [int(ans) for ans in input().split()]

    n_ones = 0
    for n in answers:
        if n == 1:
            n_ones +=1
    if n_ones >=2:
            solver_ex+=1   

print(solver_ex)
