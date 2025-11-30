#9색 20개
#180개
#23x15
import random

#판 크기
size = [6,4]

#색 종류
colors = 3

#점수
score = 0

choose = [x+1 for x in range(colors)]
choose += [0]*colors
board = [[random.choice(choose) for _ in range(size[0])] for _ in range(size[1])]
temp_board = []

def print_board():
	for i in board:
		print(i)

def Board(x,y):
	return board[y][x]

def _click(x, y, editMap):
	if (Board(x,y) != 0):
		print('빈공간이 아니네요')
		return 0
	if x < 0 or x >= size[0] or y < 0 or y >= size[1]:
		print('잘못된 좌표')
		return 0
	
	temp_board = []
	for i in board:
		l = []
		for j in i:
			l.append(j)
		temp_board.append(l)

	value_count = [0]*(colors+1)
	total = 0

	dx = [-1, 1, 0, 0]
	dy = [ 0, 0, -1, 1]
	value = [0]*4
	posX = [-1]*4
	posY = [-1]*4

	for i in range(4):
		horizontal = x + dx[i]
		vertical = y + dy[i]
		while 0 <= horizontal < size[0] and 0 <= vertical < size[1]:
			if board[vertical][horizontal] != 0:
				value[i] = board[vertical][horizontal]
				posX[i] = horizontal
				posY[i] = vertical
				break
			horizontal += dx[i]
			vertical += dy[i]
	for i in range(4):
		v = value[i]
		if 1 <= v <= colors:
			value_count[v] += 1
	
	for i in range(4):
		v = value[i]
		if(v > 0 and value_count[v] >= 2):
			horizontal = posX[i]
			vertical = posY[i]
			if(horizontal >= 0 and vertical >= 0):
				temp_board[vertical][horizontal] = 0
				if (editMap):
					board[vertical][horizontal] = 0
				total += 1
	if (editMap):
		print(f'타일 {total}개 클리어')
	return total

def click(x,y):
	return _click(x,y,True)

def click_preview(x,y):
	return _click(x,y,False)