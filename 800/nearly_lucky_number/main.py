def is_lucky_number(num):
    return num in {4, 7, 44, 47, 74, 77}

def main():
    n = int(input())

    lucky_count = 0

    while n > 0:
        digit = n % 10
        if digit == 4 or digit == 7:
            lucky_count += 1
        n //= 10
    
    print("YES" if is_lucky_number(lucky_count) else "NO")
    
if __name__ == "__main__":
    main()