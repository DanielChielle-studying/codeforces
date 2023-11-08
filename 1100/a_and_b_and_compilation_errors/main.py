def main():
    n = int(input())
    first_errors = sum(map(int, input().split()))
    second_errors = sum(map(int, input().split()))
    third_errors = sum(map(int, input().split()))

    print(first_errors - second_errors, second_errors - third_errors)

if __name__ == "__main__":
    main()
