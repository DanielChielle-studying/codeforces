def check_pa(a, b, c):
    if a - b == b - c:
        return True
    else:
        return False

def main():
    t = int(input())

    for _ in range(t):
        a, b, c = map(int, input().split())

        a_b = b - a
        a_c = (a + c) / 2
        b_c = c - b

        if a <= b - b_c and (b - b_c) % a == 0 and check_pa(b - b_c, b, c):
            print("YES")
        elif b <= a_c and a_c % b == 0 and check_pa(a, a_c, c):
            print("YES")
        elif c <= b + a_b and (b + a_b) % c == 0 and check_pa(a, b, b + a_b):
            print("YES")
        else:
            print("NO")

if __name__ == '__main__':
    main()
 