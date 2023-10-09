number_a = input()
number_b = input()

print_list = ""

for index, number in enumerate(number_a):
    if number_a[index] == number_b[index]:
        print_list += "0"
    else:   
        print_list += "1"

print(print_list)