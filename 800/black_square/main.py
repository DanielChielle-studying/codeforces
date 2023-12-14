def main():
	a = list(map(int, input().split()))	
	s = input()

	calories = 0

	for l in s:
		calories += a[int(l) - 1]		  

	print(calories)

if __name__ == '__main__':
	main()
