#    Main Author(s): Canberk Secilmez, Ali Riza Sevgili 

from a1_partc import Queue

def get_overflow_list(grid):
	rows = len(grid)
	columns = len(grid[0])
	overflow_cells = []
	for i in range(rows):
		for j in range(columns):
			neighbors = 0
			if i > 0:
				neighbors += 1
			if i < rows - 1:
				neighbors += 1
			if j > 0:
				neighbors += 1
			if j < columns - 1:
				neighbors += 1
			if abs(grid[i][j]) >= neighbors:
				overflow_cells.append((i, j))
	if overflow_cells:
		return overflow_cells
	return None

'''def get_neighbor_count(i, j, rows, columns):
    neighbors = 0
    if i > 0: neighbors += 1  
    if i < rows - 1: neighbors += 1  
    if j > 0: neighbors += 1  
    if j < columns - 1: neighbors += 1  
    return neighbors
	then I will need to change the if statments after the ocerflow cells append 
'''

def overflow(grid, a_queue):
	overflow_list = get_overflow_list(grid)
	if overflow_list == None or check_for_all_same_sign(grid):
		return 0

	d = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
	rows_len = len(grid)
	cols_len = len(grid[0])

	for cell in overflow_list:
		x, y = cell
		for dx, dy in d:
			nx, ny = x + dx, y + dy
			if 0 <= nx < rows_len and 0 <= ny < cols_len:
				increase_one_pass_sign(x, y, grid, nx, ny)

	neighbor_lists = []
	for i in range(len(overflow_list)):
		for j in range(i+1, len(overflow_list)):
			if neighbor(overflow_list[i], overflow_list[j]):
				neighbor_overflow_cell(overflow_list[i], overflow_list[j], grid)
				neighbor_lists.append(overflow_list[i])
				neighbor_lists.append(overflow_list[j])

	
	overflow_list = [cell for cell in overflow_list if cell not in neighbor_lists]

	for cell in overflow_list:
		x, y = cell
		grid[x][y] = 0
		
	new_grid = [row[:] for row in grid]
	a_queue.enqueue(new_grid)
	return 1 + overflow(grid, a_queue)

def neighbor(cell1, cell2):
	x1, y1 = cell1
	x2, y2 = cell2
	return abs(x1 - x2) + abs(y1 - y2) == 1
	

def increase_one_pass_sign(overflow_row, overflow_col, grid, row, col):
	grid[row][col] = abs(grid[row][col]) + 1
	if grid[overflow_row][overflow_col] < 0:
		grid[row][col] = -grid[row][col]
	

def positive(self):
	return self >= 0


def check_for_all_same_sign(grid):
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] != 0:
				first_sign = positive(grid[i][j])	
				break
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] != 0 and positive(grid[i][j]) != first_sign:
				return False
	return True


def neighbor_overflow_cell(c1, c2, grid):
	sign_t1 = positive(grid[c1[0]][c1[1]])
	sign_t2 = positive(grid[c2[0]][c2[1]])
	grid[c1[0]][c1[1]] = 1 if sign_t2 else -1
	grid[c2[0]][c2[1]] = 1 if sign_t1 else -1
