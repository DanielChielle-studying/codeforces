def main():
	t = int(input())

	for _ in range(t):
		l, n = map(int, input().split())
		sum_layers = l*n + n/2 * (n - 1)
		print(int(sum_layers))

if __name__ == '__main__':
	main()
