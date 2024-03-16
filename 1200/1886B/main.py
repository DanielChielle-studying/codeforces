from math import dist

def get_mid_point(ax, ay, bx, by):
	return (ax + bx) / 2, (ay + by) / 2

def main():

	t = int(input())

	for _ in range(t):
		px, py = map(int, input().split())
		ax, ay = map(int, input().split())
		bx, by = map(int, input().split())

		O = [0, 0]
		P = [px, py]
		A = [ax, ay]
		B = [bx, by]

		distance_a_p = dist(A, P)
		distance_a_o = dist(A, O)

		distance_b_p = dist(B, P)
		distance_b_o = dist(B, O)

		closer_p = (ax, ay) if distance_a_p <= distance_b_p else (bx, by)
		closer_o = (ax, ay) if distance_a_o <= distance_b_o else (bx, by)

		distance_closer_p = dist(closer_p, P)
		distance_closer_o = dist(closer_o, O)

		if closer_p == closer_o:
			print(max(distance_closer_p, distance_closer_o))
		else:
			mid_point = get_mid_point(ax, ay, bx, by)
			distance_mid = dist(A, mid_point)
			print(max(distance_mid, distance_closer_p, distance_closer_o))

if __name__ == '__main__':
	main()
