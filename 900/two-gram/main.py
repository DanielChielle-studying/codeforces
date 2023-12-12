def main():
	n = int(input())
	s = input()

	pairs = {}

	for i in range(n - 1):
		pair = s[i] + s[i + 1]

		if pair in pairs:
			pairs[pair] += 1
		else:
			pairs[pair] = 1

	print(max(pairs, key=pairs.get))

if __name__ == '__main__':
	main()
