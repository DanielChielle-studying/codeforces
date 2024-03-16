def main():
	n = input()

	fours = 0

	if n[0] == "4":
		print("NO")
	else:
		for i in n:
			if i != "1" and i != "4":
				print("NO")
				break
			else:
				if i == "4":
					fours += 1
				else:
					fours = 0
					
				if fours > 2:
					print("NO")
					break
		else:
			print("YES")
	

if __name__ == '__main__':
	main()
