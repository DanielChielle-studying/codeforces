def lucky_test(n):
    lucky_num = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

    for i in lucky_num:
        if n % i == 0:
            return "YES"
    else:
        return "NO"
    
def main():
    n = int(input())
    print(lucky_test(n))

if __name__ == "__main__":
    main()  