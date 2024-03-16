n = int(input())

words = {}
status = []

for x in range(n):
    word = input()

    if word in words:
        words[word] += 1
        w_aux = word + str(words[word])
        status.append(w_aux)
    else:
        words[word] = 0
        status.append("OK")

    print(status[x])
