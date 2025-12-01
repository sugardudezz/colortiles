from game import *
from solve import *


'''while True:
	print_board(new)
	a,b = list(map(int, input('좌표 입력').split()))
	click(a-1,b-1, new)
'''

'''result = 0
result2 = 0
for i in range(10000):
	b = Board()
	result += greedy(b.content)
for i in range(10000):
	b = Board()
	result2 += greedy2(b.content)
print(result/10000)
print(result2/10000)'''

b = Board().content
print_board(b)
print('초기 상태')
greedy2(b)