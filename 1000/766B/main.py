def main():
	n = int(input())
	lines = list(map(int, input().split()))
	lines.sort()

	i = 0
	j = 2

	while j < len(lines):
		test = lines[i:j+1]
		a = test[0]
		b = test[1]
		c = test[2]

		if a + b > c and a + c > b and b + c > a:
			print("YES")
			break
		else:
			i += 1
			j += 1
	else:
		print("NO")

if __name__ == '__main__':
	main()
