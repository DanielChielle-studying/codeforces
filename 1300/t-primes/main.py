import math

def sieve_of_eratosthenes():
    limit = (10 ** 6) + 1
    primes = [True for i in range(limit)]
    primes[0] = False
    primes[1] = False
    
    p = 2

    while p * p <= limit:
        if primes[p] == True:
            for i in range(p * p, limit, p):
                primes[i] = False
        p += 1

    return primes


primes = sieve_of_eratosthenes()

n = int(input())
numbers = list(map(int, input().split()))

for i in numbers:
    square = math.sqrt(i)
    if square.is_integer():
        square = int(square)
        if primes[square] == True:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")

