def main():
    n = input()
    s = input()

    zeros = s.count("0")
    ones = s.count("1")

    print(max(zeros, ones) - min(zeros, ones))

if __name__ == "__main__":
    main()