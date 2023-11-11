def main():    
    t = int(input())

    for _ in range(t):
        n = int(input())

        if n == 1:
            print(0)
        else:
            moves = 0
            if n != 1:
                while n != 1:
                    if n % 6 == 0:
                        n //= 6
                    elif n % 3 == 0:
                        n *= 2
                    else:
                        moves = -1
                        break
                    moves += 1
                print(moves)
            else:
                print(0)
        
if __name__ == "__main__":
    main()

    