import math

n, m, a = [int(num) for num in input().split()]

n_squares = math.ceil(n/a)
m_squares = math.ceil(m/a)

total_square = math.ceil(n_squares*m_squares)

print(total_square)