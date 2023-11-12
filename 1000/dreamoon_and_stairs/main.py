def main():
    n, m = map(int, input().split())

    if m > n:
        print(-1)
    else:
        twos = n // 2
        ones = n % 2
        moves = twos + ones

        while moves % m != 0:
            moves += 1
        
        print(moves)

if __name__ == "__main__":
    main()