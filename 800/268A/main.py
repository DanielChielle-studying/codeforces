def main():
	n = int(input())

	h_colors = []
	a_colors = []

	for _ in range(n):
		h, a = map(int, input().split())
		h_colors.append(h)
		a_colors.append(a)

	count = 0	

	for i in range(n):
		for j in range(n):
			if i != j:
				if h_colors[i] == a_colors[j]:
					count += 1

	print(count)
	
if __name__ == '__main__':
	main()
