number_words = int(input())

words = {}
final_words = []

for index in range(number_words):
    words[index] = input()
    if len(words[index]) <= 10:
        final_words.append(words[index])
    else:
        f_letter = words[index][0]
        fn_letter = words[index][-1]
        size = len(words[index]) - 2
        final_words.append(f_letter + str(size) + fn_letter)

for word in final_words:
    print(word)