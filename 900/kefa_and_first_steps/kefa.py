n = int(input())
values = [int(value) for value in input().split()]

sequence = []
sequence.append(values[0])
max_sequence = []

for a in values[1:]:
    if a >= sequence[-1]:
        sequence.append(a)
    else:
        sequence.clear()
        sequence.append(a)

    max_sequence.append(len(sequence)) 

print(max(max_sequence)) if max_sequence else print(1)