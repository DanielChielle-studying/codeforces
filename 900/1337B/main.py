def can_defeat_dragon(x, n, m):
    while n > 0 and x > 20:
        x = x // 2 + 10
        n -= 1
    return x <= m * 10

def main():
    t = int(input())

    for _ in range(t):
        x, n, m = map(int, input().split())
        if can_defeat_dragon(x, n, m):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()
