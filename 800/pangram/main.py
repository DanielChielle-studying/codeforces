def main():
	n = input()
	p = set(input().lower())

	if len(p) >= 26:
		print("YES")
	else:
		print("NO")

if __name__ == '__main__':
	main()
