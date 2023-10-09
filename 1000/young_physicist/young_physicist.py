number_of_cordinates = int(input())

cordinates = {}

final_a = 0
final_b = 0
final_c = 0

for index in range(number_of_cordinates):
    cordinates[index] = a, b, c = [int(num) for num in input().split()]

    final_a += cordinates[index][0]
    final_b += cordinates[index][0]
    final_c += cordinates[index][0]

if final_a == 0 and final_b == 0 and final_c == 0:
    print("YES")
else:
    print("NO")