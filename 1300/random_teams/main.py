from math import comb

def main():
	n, m = map(int, input().split())

	# maximum number of pairs
	max_pairs = comb(n - m + 1, 2)

	if m == 1:
		min_pairs = max_pairs
	else:
		#minimun number of pairs
		div = n // m
		rest = n % m

		min_pairs = (m - rest) * comb(div, 2)
		if rest != 0:
			min_pairs += rest * comb(div + 1, 2)

	print(min_pairs, max_pairs)

if __name__ == '__main__':
	main()
