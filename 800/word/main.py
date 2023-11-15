def main():
    s = input()

    upper = 0
    lower = 0

    for l in s:
        if l.isupper():
            upper += 1
        else:
            lower += 1
    
    if lower >= upper:
        print(s.lower())
    else:
        print(s.upper())

if __name__ == "__main__":
    main()