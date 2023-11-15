def main():
    k, n, w = map(int, input().split())

    cost = 0

    for i in range(1, w+1):
        cost += k * i

    print(0 if cost <= n else cost - n)

if __name__ == "__main__":
    main()