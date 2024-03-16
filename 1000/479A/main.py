a = int(input())
b = int(input())
c = int(input())

possibilit_1 = a+b+c
possibilit_2 = a*b*c
possibilit_3 = a+b*c
possibilit_4 = a*b+c
possibilit_5 = (a+b) * c
possibilit_6 = a*(b+c)

higher_number = max(possibilit_1, possibilit_2, possibilit_3, possibilit_4, possibilit_5, possibilit_6)
print(higher_number)