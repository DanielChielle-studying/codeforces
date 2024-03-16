t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    print(k + (k - 1) // (n - 1))



# quantos numeros divisiveis por 3 existem entre 1 e 7?
# para cada numero divisil por 3, o "7" deve ser descolado para a direita


# x + 2x + 3x + 4x + 5x ...... 


# 7...8...9...

# k - 1 / n - 1

# [1, 2, 3, 4, 5, 6, 7]
# [3, 6]
# 7 -> 8 -> 9 ?

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# [4, 8, 12]
# 12 -> 13 -> 14 -> 15


# 7 - 1 // 3 - 1 = 3?
# 12 - 1 // 4 - 1 = 3?