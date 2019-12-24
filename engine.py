from random import choice

def control(grid):
	"""
		This function accepts input and marks the player’s cells.
		(grid) -- the value of the cells (1-9)
	"""
	cell = int(input(":")) - 1 # because cells begin with 1
	grid[cell] = "X"
	return grid # return modified list (add your pos)

def logic(grid):
	"""
		This function checks the position of the cells and returns the status
		of the game (True - the game continues, False - the game is finished).
		(grid) -- the value of the cells (1-9)
	"""
	# it's so bad, i'm sorry
	if grid[:3] == ["X", "X", "X"] or grid[3:6] == ["X", "X", "X"] or grid[6:9] == ["X", "X", "X"] or \
	grid[::3] == ["X", "X", "X"] or grid[1::3] == ["X", "X", "X"] or grid[2::3] == ["X", "X", "X"] or \
	grid[::4] == ["X", "X", "X"] or grid[2:8:2] == ["X", "X", "X"]:
		input("You Won! Congratulations!\nEnter to continue..........")
		return False
	elif grid[:3] == ["O", "O", "O"] or grid[3:6] == ["O", "O", "O"] or grid[6:9] == ["O", "O", "O"] or \
	grid[::3] == ["O", "O", "O"] or grid[1::3] == ["O", "O", "O"] or grid[2::3] == ["O", "O", "O"] or \
	grid[::4] == ["O", "O", "O"] or grid[2:8:2] == ["O", "O", "O"]:
		input("You Lose!\nEnter to continue..........")
		return False
	elif [cell for cell in grid if cell != "X" and cell != "O"] == []:
		input("Game Over!\nEnter to continue..........")
		return False
	return True # return modified status (example: You Won -- 'False', You Lose -- 'False')

def enemy(grid):
	"""
		This function mimics the behavior of an adversary, in
		fact, it simply selects a random free cell and marks it.
		(grid) -- the value of the cells (1-9)
	"""
	# it's so bad again, i'm sorry
	try:	
		cell = choice([cell for cell in range(9) if grid[cell] != "X" and grid[cell] != "O"]) # choose a random cell not occupied by a player or himself
		grid[cell] = "O"
	except:
		pass
	return grid # return modified list (add enemy pos)