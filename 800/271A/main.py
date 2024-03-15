def main():
	y = int(input())
	
	while True:
		y += 1
		a = str(y)

		if len(set(a)) == len(a):
			print(a)
			break
	
if __name__ == '__main__':
	main()
