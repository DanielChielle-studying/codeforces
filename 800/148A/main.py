def main():
	k = int(input())
	l = int(input())
	m = int(input())
	n = int(input())
	d = int(input())

	damage = [k, l, m, n]
	numbers = [i for i in range(1, d + 1)]
	result = []

	for n in numbers:
		for dmg in damage:
			if n % dmg == 0:
				result.append(True)
				break

	print(len(result))


if __name__ == '__main__':
	main()
