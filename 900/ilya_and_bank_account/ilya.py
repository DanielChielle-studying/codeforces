def remove_max_digit(number):
    last_d = number[-1]
    blast_d = number[-2]
    number = number[:-2]

    if last_d > blast_d:
        number += blast_d
    else:
        number += last_d

    return number

balance = input()

if int(balance) < 0:
    balance = remove_max_digit(balance)

print(int(balance))