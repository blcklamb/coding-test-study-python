# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
size = int(input())
park_info = [[] for _ in range(size)]
danpung = []

for i in range(size):
	row_info = list(map(int, input().split()))
	for j in row_info:
		if j==0:
			danpung.append((i, j))
	park_info[i] = row_info

def allDanpung(map_info):
	all_sum = 0
	for row in map_info:
		all_sum += sum(row)
	if all_sum == 0:
		return True
	return False

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def affectedDanpung(map_info):
	will_be_danpung = []
	for i in range(size):
		for j in range(size):
			if map_info[i][j] != 0:
				surr_danpungs = 0
				for k in range(4):
					surrR, surrC = i+dr[k], j+dc[k]
					if 0<=surrR<size and 0<=surrC<size and map_info[surrR][surrC] == 0:
						surr_danpungs += 1
				will_be_danpung.append((i, j, surr_danpungs))
	for will_info in will_be_danpung:
		r, c, howMuch = will_info
		map_info[r][c] -= howMuch
		if map_info[r][c] < 0:
			map_info[r][c] = 0
	return map_info
	
day = 0	
while not allDanpung(park_info):
	park_info = affectedDanpung(park_info)
	day += 1
	
print(day)
