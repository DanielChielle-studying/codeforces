def main():
    t = int(input())

    l = "abcdefghijklmnopqrstuvwxyz"
    
    for _ in range(t):
        n, a, b = map(int, input().split())
        s = ((l[:b]*n)[:n])
        print(s)

if __name__ == "__main__":
    main()

