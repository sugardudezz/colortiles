from game import *

def get_possible_moves(b):
	ret = []
	for y in range(size[1]):
		for x in range(size[0]):
			if (b[y][x] == 0):
				prev = click_preview(x,y,b)
				if len(prev.removed) > 0:
					ret.append([x,y,len(prev.removed)])
	return ret

def tiles_left(b):
	zeros = 0
	for row in b:
		zeros += row.count(0)
	return size[0]*size[1] - zeros


def greedy2(board):
	solution = []
	while True:
		moves = get_possible_moves(board)
		if len(moves) == 0:
			print(f'greedy2 sol: {solution}')
			print(f'tiles left: {tiles_left(board)}')
			return tiles_left(board)
		
		odd_colors = []

		for c in range(colors):
			c = c+1
			if (board.count(c)) % 2 == 1:
				odd_colors.append(c)
		
		evaluation = [0]*len(moves)

		for i in range(len(moves)):
			temp_board = copy.deepcopy(board)
			click(moves[i][0], moves[i][1], temp_board)
			evaluation[i] += (len(get_possible_moves(temp_board)))

			temp_odd_colors = []
			for c in range(colors):
				c = c+1
				if (board.count(c)) % 2 == 1:
					temp_odd_colors.append(c)
			
			if len(temp_odd_colors) < len(odd_colors):
				evaluation[i] *= size[0]*size[1]


		best = moves[evaluation.index(max(evaluation))]

		if (best):
			cleared = click(best[0], best[1], board)
			print_board(board)
			print(f'타일 {len(cleared.removed)}개 클리어')
			solution.append(best)