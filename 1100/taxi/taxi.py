number_groups = int(input())
groups = ([int(group) for group in input().split()])
total_taxis = 0

one = 0
two = 0
three = 0
four = 0

for n in groups:
    if n == 4:
        four+=1
    elif n == 3:
        three+=1
    elif n == 2:
        two+=1
    else:
        one+=1

total_four = 0
total_three = 0
total_two = 0
total_one = 0
total_taxis = 0

total_four = four
total_three = three
total_two = two // 2
rest_two = two % 2

if one > three:
    rest_one = one - three

    one_t = rest_one // 4
    one_r = rest_one % 4

    if rest_two == 1:
        o_and_t = one_r + 2*rest_two
        ot_t = o_and_t // 4
        ot_r = o_and_t % 4 
        total_one = one_t + ot_t +int(bool(ot_r))
    else:
        total_one += one_t + int(bool(one_r))
        
else:
    total_two += rest_two


total_taxis = total_four + total_three + total_two + total_one


print(int(total_taxis))


