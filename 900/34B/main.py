def main():
    n, m = map(int, input().split())
    tvs = sorted(list(map(int, input().split())))

    sum_momey = 0

    for i in range(m):
        if tvs[i] <= 0:
            sum_momey += tvs[i]
        else:
            break

    print(-1*sum_momey)

if __name__ == "__main__":
    main()