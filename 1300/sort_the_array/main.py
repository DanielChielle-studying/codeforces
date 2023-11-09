def main():
    n = int(input())
    a = list(map(int, input().split()))

    a_sorted = sorted(a)

    if a == a_sorted:
        print("yes")
        print("1 1")
    else:
        first = 1 
        while first < n and a[first] > a[first - 1]:
           first += 1

        last = n
        while last > 1 and a[last - 2] < a[last - 1]:
            last -= 1

        segment = a[first - 1:last][::-1]
        
        if a[:first - 1] + segment + a[last:] == a_sorted:
            print("yes")
            print(first, last)
        else:
            print("no")

if __name__ == "__main__":
    main()