def main():
	n = int(input())
	p = input().split()
	q = input().split()

	s = set(p[1:] + q[1:])
	
	if len(s) == n:
		print("I become the guy.")
	else:
		print("Oh, my keyboard!")
		
if __name__ == '__main__':
	main()
