n_lanterns, street_l = map(int, input().split())
lanters = sorted([int(l) for l in input().split()])

lanters_distance = 0
first_distance = lanters[0]
last_distance = street_l - lanters[-1]

for l, l2 in zip(lanters[:-1], lanters[1:]):
    distance = l2-l
    if distance > lanters_distance:
        lanters_distance = distance


print(max(first_distance, last_distance, lanters_distance / 2))

