def main():
	host = input()
	guest = input()
	pile = sorted(input())

	if sorted(host + guest) == pile:
		print("YES")
	else:
		print("NO")

if __name__ == '__main__':
	main()
