word = input()

first_letter = word[0]
rest_word = word[1:]

first_is_cap = True if first_letter.isupper() else False

if word.isupper():
    print(word.lower())
elif len(word) == 1:
    print(word.capitalize())
elif first_is_cap == False and rest_word.isupper():
    word = word.lower()
    print(word.capitalize())
else:
    print(word)

