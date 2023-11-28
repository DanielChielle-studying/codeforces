from math import sqrt

def get_distance(ax, ay, bx = 0, by = 0):
	return sqrt((bx - ax)**2 + (by - ay)**2)

def get_mid_point(ax, ay, bx, by):
	return (ax + bx) / 2, (ay + by) / 2

def main():

	t = int(input())

	for _ in range(t):
		px, py = map(int, input().split())
		ax, ay = map(int, input().split())
		bx, by = map(int, input().split())

		distance_a_p = get_distance(ax, ay, px, py)
		distance_b_p = get_distance(bx, by, px, py)

		distance_a_o = get_distance(ax, ay)
		distance_b_o = get_distance(bx, by)

		closer_p = (ax, ay) if distance_a_p <= distance_b_p else (bx, by)
		closer_o = (ax, ay) if distance_a_o <= distance_b_o else (bx, by)

		distance_closer_p = get_distance(closer_p[0], closer_p[1], px, py)
		distance_closer_o = get_distance(closer_o[0], closer_o[1])

		if closer_p == closer_o:
			print(max(distance_closer_p, distance_closer_o))
		else:
			mid_point = get_mid_point(ax, ay, bx, by)
			distance_mid = get_distance(ax, ay, mid_point[0], mid_point[1])
			print(max(distance_mid, distance_closer_p, distance_closer_o))

if __name__ == '__main__':
	main()
