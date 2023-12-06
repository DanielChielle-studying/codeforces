from math import sqrt

def main():
    l, k = map(int, input().split())
    current_side = l

    for _ in range(k):
        current_side = sqrt(current_side**2 / 2)

    formated_result = "{:.20f}".format(current_side**2)
    print(formated_result)

if __name__ == "__main__":
    main()