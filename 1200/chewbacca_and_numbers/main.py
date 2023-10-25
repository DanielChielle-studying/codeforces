number = input()
f_num = ""
for i, n in enumerate(number):
    num = int(n)
    inverted_num = 9 - num
    if inverted_num < num and (inverted_num > 0 or i > 0):
        f_num += str(inverted_num)
    else:
        f_num += n

print(f_num)

