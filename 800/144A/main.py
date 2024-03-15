def main():
	n = int(input())
	soldiers = list(map(int, input().split()))
	l = soldiers[0]
	l_index = 0
	h = soldiers[0]
	h_index = 0

	for s in range(n):
		if soldiers[s] <= l:
			l = soldiers[s]
			l_index = s
		elif soldiers[s] > h:
			h = soldiers[s]
			h_index = s

	if h_index > l_index:
		print(n - l_index + h_index - 2)
	else:
		print(n - l_index + h_index - 1)

if __name__ == '__main__':
	main()
