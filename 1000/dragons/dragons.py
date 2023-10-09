kito_s, n_dragons = [int(value) for value in input().split()]

dragon_info = {}

for d in range(n_dragons):
    strength, bonus = [int(value) for value in input().split()]
    dragon_info[d] = {
        'strength': strength,
        'bonus': bonus
    }

def ordenar_por_forca(dragon):
    return dragon_info[dragon]['strength']
dragons_sorted = sorted(dragon_info.keys(), key=ordenar_por_forca)

for dragon in dragons_sorted:
    if kito_s > dragon_info[dragon]['strength']:
        kills_everything = True
        kito_s+=dragon_info[dragon]['bonus']
    else:
        kills_everything = False

print("YES") if kills_everything else print("NO")