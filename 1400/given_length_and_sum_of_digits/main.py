def main():
    m, s = map(int, input().split())

    if s == 0 and m == 1:
        print("0 0")
    elif s / m > 9 or s == 0:
        print("-1 -1")
    else:
        number = ""
        while s > 0:
            if s >= 9:
                number += "9"
                s -= 9
            else:
                number += str(s)
                s = 0

        max_number = number + "0" * (m - len(number))
        min_number = max_number[::-1]
        
        if min_number[0] == "0":
            digits = [int(d) for d in min_number]
            digits[0] += 1

            for i in range(1, len(digits)):
                if digits[i] > 0:
                    digits[i] -= 1
                    break

            min_number = ''.join([str(d) for d in digits])

        print(min_number, max_number)

if __name__ == '__main__':
    main()
