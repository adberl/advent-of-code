f = [i.rstrip() for i in open('input', 'r').readlines()]

draw_numbers = [int(i) for i in f[0].split(',')]
boards = []

class Board:
	def __init__(self, board):
		self.rows = []
		for row in board:
			self.rows.append([(int(i.strip()), 0) for i in row.split(' ') if not i == ''])

	def __str__(self):
		tmp_str = ""
		for row in self.rows:
			#wtf is this
			tmp_str += "".join(map(lambda x : str(x[0]) + f"{'x' if x[1] == 1 else ''} ", row)) + "\n"
		return tmp_str

	def draw_number(self, draw_num):
		for row in self.rows:
			for i in range(len(row)):
				if row[i][0] == draw_num:
					row[i] = (row[i][0], 1)
					return self.test_win()

	def test_win(self):
		return self.test_rows() + self.test_colums()

	def test_rows(self):
		for row in self.rows:
			if sum(n[1] for n in row)  == 5:
				return 1
		return 0
	
	def test_colums(self):
		for i in range(len(self.rows)):
			tmp_sum = 0
			for j in range(len(self.rows[0])):
				tmp_sum += self.rows[j][i][1] # row j and column i
			if tmp_sum == 5:
				return 1
			tmp_sum = 0
		return 0

	def sum_unmarked(self):
		fin_sum = 0
		for row in self.rows:
			fin_sum += sum(n[0] for n in row if n[1] == 0)
		return fin_sum

def init_boards():
	temp_board = []

	for line in f:
		if line == '':
			boards.append(Board(temp_board))
			temp_board.clear()
		else:
			temp_board.append(line)

def start_draw_numbers():
	# when drawing number, test it against all 
	for i in draw_numbers:
		for board in boards:
			if(board.draw_number(i) == 1):
				return board.sum_unmarked() * i

def print_boards():
	for board in boards:
		print(board)

f.pop(0)
f.pop(0)

init_boards()
print(start_draw_numbers())
#print_boards()