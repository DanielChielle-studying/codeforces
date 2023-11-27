def main():

	n, h = map(int, input().split())
	a = list(map(int, input().split()))
	
	width = 0

	for i in a:
		width += 1 if i <= h else 2

	print(width)

if __name__ == '__main__':
	main()
