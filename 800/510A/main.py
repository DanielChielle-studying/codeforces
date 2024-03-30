def main():
    n, m = map(int, input().split())
    ground = [["."]*m for _ in range(n)]
    
    jump = False
    right = True
    for i in range(n):
        if jump == False:
            ground[i] = ["#"]*m
            jump = True
        else:
            if right:
                ground[i][-1] = "#"
                right = False
            else:
                ground[i][0] = "#"
                right = True
            jump = False

    for row in ground:
        print("".join(row))

if __name__ == '__main__':
    main()
