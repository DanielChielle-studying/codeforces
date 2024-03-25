def main():
	t = int(input())

	for _ in range(t):
		n = int(input())
		values = list(map(int, input().split()))

		groups = []
		current_group = [values[0]]
		max_sum = 0

		for i in range(1, n):
			if (values[i] >= 0 and values[i-1] >= 0) or (values[i] <= 0 and values[i-1] <= 0):
				current_group.append(values[i])
			else:
				groups.append(current_group)
				max_sum += max(current_group)
				current_group = [values[i]]
				
		max_sum += max(current_group)
		groups.append(current_group)
		
		print(max_sum)

if __name__ == '__main__':
	main()
