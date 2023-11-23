def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        difference = {}
        pairs = 0

        for i in range(n):
            diff = a[i] - i

            if diff in difference:
                pairs += difference[diff]
                difference[diff] += 1
            else:
                difference[diff] = 1

        print(pairs)

if __name__ == "__main__":
    main()