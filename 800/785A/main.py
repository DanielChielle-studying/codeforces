def main():	
	n = int(input())
	total = 0

	for _ in range(n):
		p = input()

		if p[0] == "T":
			total += 4
		elif p[0] == "C":
			total += 6
		elif p[0] == "O":
			total += 8
		elif p[0] == "D":
			total += 12
		else:
			total += 20

	print(total)

if __name__ == '__main__':
	main()
