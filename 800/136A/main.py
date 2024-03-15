def main():
	n = int(input())
	p = list(map(int, input().split()))
	final_p = [0] * n

	for i in range(n):
		final_p[p[i] - 1] = i + 1

	for a in final_p:
		print(a)

if __name__ == '__main__':
	main()
