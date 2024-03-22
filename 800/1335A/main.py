def main():

	n = int(input())

	for _ in range(n):
		candies = int(input())
		if candies % 2 == 0:
			candies -= 1
		print(int(candies / 2))

if __name__ == '__main__':
	main()
