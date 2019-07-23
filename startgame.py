import tictactoe

print("Let's play Tic Tac Toe with an Artificial Intelligence")

playerScore = 0
computerScore = 0
ties = 0
numGamesPlayed = 0
while True:
	# Reset the board
	board = [' '] * 10
	numGamesPlayed += 1
	playerLetter, computerLetter = tictactoe.inputPlayerLetter()
	turn = tictactoe.whoGoesFirst()
	print('The ' + turn + ' will go first.')
	gameIsPlaying = True

	while gameIsPlaying:
		if turn == 'player':
			# Player's turn
			tictactoe.drawBoard(board)
			move = tictactoe.getPlayerMove(board)
			tictactoe.makeMove(board, playerLetter, move)

			if tictactoe.isWinner(board, playerLetter):
				# Player won game
				playerScore += 1
				tictactoe.drawBoard(board)
				print('Congratulations! You have won the game!')
				print('Player wins:'+ str(playerScore) + ' Computer wins:'+ str(computerScore)+ ' Ties:'+ str(ties)+ ' Games Played:'+ str(numGamesPlayed))
				gameIsPlaying = False
			else:
				if tictactoe.isBoardFull(board):
					# Tie game
					ties += 1
					tictactoe.drawBoard(board)
					print('The game is a tie.')
					print('Player wins:'+ str(playerScore) + ' Computer wins:'+ str(computerScore)+ ' Ties:'+ str(ties)+ ' Games Played:'+ str(numGamesPlayed))
					break
				else:
					turn = 'computer'

		if turn == 'computer':
			move = tictactoe.getComputerMove(board, computerLetter)
			tictactoe.makeMove(board, computerLetter, move)

			if tictactoe.isWinner(board, computerLetter):
				# Computer won game
				computerScore += 1
				tictactoe.drawBoard(board)
				print('The computer has beaten you! You lose!')
				print('Player wins:'+ str(playerScore) + ' Computer wins:'+ str(computerScore)+ ' Ties:'+ str(ties)+ ' Games Played:'+ str(numGamesPlayed))
				gameIsPlaying = False
			else:
				if tictactoe.isBoardFull(board):
					# Tie game
					ties += 1
					tictactoe.drawBoard(board)
					print('The game is a tie.')
					print('Player wins:'+ str(playerScore) + ' Computer wins:'+ str(computerScore)+ ' Ties:'+ str(ties)+ ' Games Played:'+ str(numGamesPlayed))
					break
				else:
					turn = 'player'
	if not tictactoe.playAgain():
		break