from math import ceil

def main():
	n, m = map(int, input().split())
	children = list(map(int, input().split()))

	div = 0

	for i in range(n):
		if ceil(children[i] / m) >= div:
			div = ceil(children[i] / m)
			max_child = i

	print(max_child + 1)

if __name__ == '__main__':
	main()
