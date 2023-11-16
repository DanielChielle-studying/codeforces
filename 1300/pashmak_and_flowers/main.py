def main():
    n = int(input())
    b = list(map(int, input().split()))

    smallest = min(b)
    biggest = max(b)

    diff = biggest - smallest

    count_smallest = b.count(smallest)
    count_biggest = b.count(biggest)

    if smallest == biggest:
        possibilities = n * (n - 1) // 2
    else:
        possibilities = count_smallest * count_biggest

    print(diff, possibilities)    
    
if __name__ == "__main__":
    main()