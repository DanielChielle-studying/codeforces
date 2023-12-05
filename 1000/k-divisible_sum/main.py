from math import ceil

def main():
	t = int(input())

	for _ in range(t):
		n, k = map(int, input().split())

		min_sum = ceil(n / k) * k
		max_value = (min_sum + n - 1) // n

		print(max_value)

if __name__ == '__main__':
	main()
