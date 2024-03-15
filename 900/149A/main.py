def main():
	k = int(input())
	a = list(map(int, input().split()))

	a.sort(reverse=True)

	growth = 0
	months = 0

	for i in a:
		if growth >= k:
			break

		growth += i
		months += 1

	print(months if growth >= k else -1)

if __name__ == '__main__':
	main()
