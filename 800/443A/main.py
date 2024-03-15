def main():
	s = input()
	letters = s.strip("{}").replace(", ", "")
	distinct_l = set(letters)
	print(len(distinct_l))

if __name__ == '__main__':
	main()
