word = input()

hello = "hello"
word_clean = ""
index=0

for letter in hello:
    find_letter = word.find(hello[index])
    if find_letter != -1:
        word_clean += letter
        word = word[find_letter+1:]
    index+=1

if "hello" in word_clean:
    print("YES")
else:
    print("NO")