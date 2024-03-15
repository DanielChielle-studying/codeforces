def main():
	n = input()
	d = list(map(int, input().split()))

	print("HARD" if d.count(1) > 0 else "EASY")

if __name__ == '__main__':
	main()
