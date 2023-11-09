# t minutos
# n books
# a list of books
# ai minutes for each book

# will start reading from book i
# and go on i + 1, i + 2...
# he will stop when his time is out or he read the last book

# if he doest have enought time to read the nest book entirely, he will stop

def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))

    max_books = 0
    total_time = 0
    first = 0

    for i in range(n):
        total_time += a[i]
        while total_time > t:
            total_time -= a[first]
            first += 1
        max_books = max(max_books, i - first + 1)
    
    print(max_books)

if __name__ == "__main__":
    main()