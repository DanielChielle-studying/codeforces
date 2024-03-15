situation = input()

dangerous_level = 0
c_player = situation[0]

for player in situation:
    if(player == c_player):
        dangerous_level+=1
    else:
        dangerous_level = 1

    c_player = player

    if(dangerous_level >= 7): 
        print("YES")
        break

if(dangerous_level < 7):
    print("NO")

