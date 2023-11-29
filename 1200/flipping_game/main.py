def main():
	n = int(input())
	a = list(map(int, input().split()))

	ones = a.count(1)

	if ones == n:
		print(ones - 1)
	else:
		zeros_seq = 0
		zeros_max = 0

		for num in a:
			if num == 0:
				zeros_seq += 1
				zeros_max = max(zeros_max, zeros_seq)
			else:
				zeros_seq = max(0, zeros_seq - 1)
				
		print(ones + zeros_max)

if __name__ == '__main__':
	main()
