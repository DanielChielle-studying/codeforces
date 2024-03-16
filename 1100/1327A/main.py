def main():
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())

        if (k + n) % 2 == 0 and k * k <= n:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()