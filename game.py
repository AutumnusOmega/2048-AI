# Modified from source at https://www.geeksforgeeks.org/2048-game-in-python/



# game.py

# importing the logic.py file
# where we have written all the
# logic functions used.
import logic

# Driver code
if __name__ == '__main__':
	
# calling start_game function
# to initialize the matrix
	mat = logic.start_game()
	logic.print_board(mat)
	score = 0

while(True):

	# taking the user input
	# for next step
	x = input("Press the command : ")

	# we have to move up
	if(x == 'W' or x == 'w'):

		# call the move_up function
		mat, flag, score_change = logic.move_up(mat)

		# get the current state and print it
		status = logic.get_current_state(mat)
		print(status)
		score += score_change
		print("Score:", score)

		# if game not over then continue
		# and add a new two
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)

		# else break the loop
		else:
			break

	# the above process will be followed
	# in case of each type of move
	# below

	# to move down
	elif(x == 'S' or x == 's'):
		mat, flag, score_change = logic.move_down(mat)
		status = logic.get_current_state(mat)
		print(status)
		score += score_change
		print("Score:", score)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		else:
			break

	# to move left
	elif(x == 'A' or x == 'a'):
		mat, flag, score_change = logic.move_left(mat)
		status = logic.get_current_state(mat)
		print(status)
		score += score_change
		print("Score:", score)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		else:
			break

	# to move right
	elif(x == 'D' or x == 'd'):
		mat, flag, score_change = logic.move_right(mat)
		status = logic.get_current_state(mat)
		print(status)
		score += score_change
		print("Score:", score)
		if(status == 'GAME NOT OVER'):
			logic.add_new_2(mat)
		else:
			break
	else:
		print("Invalid Key Pressed")

	# print the matrix after each
	# move.
	logic.print_board(mat)
