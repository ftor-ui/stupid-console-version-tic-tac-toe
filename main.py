import view
import engine

# initialization
status_game = True
grid = [cell for cell in range(1, 10)]

# gameloop
while status_game:
	view.draw(grid)
	grid = engine.control(grid)
	grid = engine.enemy(grid)
	status_game = engine.logic(grid)