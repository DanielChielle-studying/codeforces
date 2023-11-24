def main():
	t = int(input())

	for _ in range(t):
		x, y = map(int, input().split())
		a, b = map(int, input().split())
		
		smallest = min(x, y)
		cost = a * abs(x - y)
		
		if 2 * a <= b:	
			cost += 2 * a * smallest
		else:
			cost += b * smallest

		print(cost)

if __name__ == '__main__':
	main()
