def main():
	n, m = map(int, input().split())
	
	lang_1_to_2 = {}

	for _ in range(m):
		l1, l2 = input().split()
		lang_1_to_2[l1] = l2

	lecture_text = input().split()
	final_text = ''

	for word in lecture_text:
		if len(word) <= len(lang_1_to_2[word]):
			final_text += word + ' '
		else:
			final_text += lang_1_to_2[word] + ' '
	
	print(final_text)

if __name__ == '__main__':
	main()


