n_fences, piano_w = map(int, input().split())
fences = [int(task) for task in input().split()]

smallest = sum(fences[:piano_w])
fences_h = sum(fences[:piano_w])
fence_position = 1

i1 = 1


if piano_w == 1:
    smallest = min(fences)
    for i, a in enumerate(fences):
        if a == smallest:
            print(i+1)
            break
else:
    for current_f, next_f in zip(fences[0:], fences[piano_w:]):
        sum_fences = fences_h - current_f + next_f

        i1 += 1
        fences_h = sum_fences

        if fences_h < smallest:
            smallest = sum_fences
            fence_position = i1

    print(fence_position)
