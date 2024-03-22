def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        skills = [0] * (n + 1)
        for s in a:
            skills[s] += 1

        skills = [x for x in skills if x != 0]
        skills.sort(reverse=True)

        diff = len(skills) - 1
        
        if skills[0] - diff >= 2:
            max_team_size = diff + 1
        else:
            max_team_size = min(skills[0], diff)

        print(max_team_size)

if __name__ == '__main__':
    main()
