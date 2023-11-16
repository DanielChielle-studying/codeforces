def find_pile(query, piles):
    left, right = 0, len(piles) - 1

    while left <= right:
        mid = (left + right) // 2
        start, end = piles[mid]
        
        if start <= query <= end:
            return mid + 1
        elif query < start:
            right = mid - 1
        else:
            left = mid + 1

    return -1

def main():

    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    q = list(map(int, input().split()))

    piles = {}
    piles[0] = (1, a[0])

    for i in range(1, n):
        piles[i] = (piles[i-1][1] + 1, piles[i-1][1] + a[i])

    for query in q:
        pile = find_pile(query, piles)
        print(pile)

if __name__ == "__main__":
    main()
