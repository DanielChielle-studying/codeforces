def main():

	n = int(input())

	current_passengers = 0
	max_passengers = 0

	for _ in range(n):
		a, b = map(int, input().split())

		current_passengers += b - a
		max_passengers = max(max_passengers, current_passengers)

	print(max_passengers)

if __name__ == '__main__':
	main()
