word = input().lower()

word = "".join([c for c in word if c not in 'aeiouy'])
new_word = ""

for i in range(len(word)):
    new_word += '.' + word[i]

print(new_word)
