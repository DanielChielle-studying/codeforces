def main():
	n, a, b = map(int, input().split())
	print(min(n - a, b + 1))

if __name__ == '__main__':
	main()
