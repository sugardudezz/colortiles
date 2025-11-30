from game import *

def get_possible_moves():
	ret = []
	for y in range(size[1]):
		for x in range(size[0]):
			if (board[y][x] == 0):
				prev = click_preview(x,y)
				if prev > 0:
					ret.append([x,y,prev])
	return ret

solution = []
def greedy():
	while True:
		moves = get_possible_moves()
		if len(moves) == 0:
			print(f'sol: {solution}')
			return
		
		check = None
		for i in [4,3,2]:
			for m in moves:
				if (m[2] == i):
					check = m
					break
			if check != None:
				break
		
		if (check):
			click(check[0], check[1])
			print_board()
			solution.append(check)

'branch and bound 알고리즘 생각'

'''
def branch_and_bound():
	moves = get_possible_moves()
	if len(moves) == 0:
		print(f'sol: {solution}')
		return
	
	check = None
	for i in [4,3,2]:
		for m in moves:
			if (m[2] == i):
				check = m
				break
		if check != None:
			break
	
	click(check[0], check[1])
	print_board()
	solution.append(check)
'''