def main():
	n, m, k = map(int, input().split())
	players_army = []

	for _ in range(m + 1):
		players_army.append(bin(int(input()))[2:]) 

	fedor = players_army[-1]
	friends = 0

	for j in players_army[:-1]:
		diff = 0
		
		max_length = max(len(fedor), len(j))
		fedor = fedor.zfill(max_length)
		j = j.zfill(max_length)
		
		for bit1, bit2 in zip(fedor, j):
			if bit1 != bit2:
				diff += 1
		if diff <= k:
			friends += 1

	print(friends)

if __name__ == '__main__':
	main()

