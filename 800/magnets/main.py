def main():
	n = int(input())
	f_m = input()

	groups = 1

	for _ in range(1, n):
		magnet = input()
		if f_m != magnet:
			groups += 1

		f_m = magnet 

	print(groups)

if __name__ == '__main__':
	main()


	