def main():
	n, x = map(int, input().split())
	count = 0

	i = 1
	j = n

	while i <= n and j >= 1:
		if i * j == x:
			count += 1
			i += 1
			j -= 1
		elif i * j < x:
			i += 1
		else:
			j -= 1

	print(count)

if __name__ == '__main__':
	main()
