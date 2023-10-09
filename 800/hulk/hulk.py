n = int(input())

phrase = ""

for a in range(1, n + 1):
    if a % 2 == 0:
        phrase += "I love "
    else:
        phrase += "I hate "
    if a < n:
        phrase += "that "

phrase += "it"

print(phrase)   