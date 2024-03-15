def main():
	n = int(input())

	bills = [100, 20, 10, 5, 1]
	count = 0
	i = 0

	while n > 0:
		count += n // bills[i]
		n = n % bills[i]
		i += 1
	
	print(count)
if __name__ == '__main__':
	main()
