from os import system, name

def clear_screan():
	"""
		Clear screan.
	"""
	system("cls" if name == "nt" else "clear")

def draw(grid):
	"""
		Draws a game field.
	"""
	clear_screan()
	line = 0
	for cell in grid:
		line += 1
		if line == 3:
			print(cell)
			line = 0
		else:
			print(cell, end="")