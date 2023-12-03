def main():
	year = int(input())
	
	while True:
		a = str(year + 1)
		if len(set(a)) == len(a):
			print(a)
			break
	
		year += 1

if __name__ == '__main__':
	main()
