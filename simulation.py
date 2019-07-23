import tictactoe

# Random Player Simulation for Tic Tac Toe against an AI

playerScore = 0
computerScore = 0
ties = 0
numGamesPlayed = 0
totalGames = 0
turn = ''
print('Random Player Simulation for Tic Tac Toe against an AI')
first = input('Who goes first? (p or c) ').lower()
if first == 'p':
	turn = 'player'
else:
	turn = 'computer'
totalGames = int(input('How many games? '))
while numGamesPlayed < totalGames:
	numGamesPlayed += 1
	board = [' '] * 10
	playerLetter, computerLetter = tictactoe.inputPlayerLetter()
	playerGoesFirst = False
	gameIsPlaying = True

	while gameIsPlaying:
		if turn == 'player':
			# Player's turn
			# Player makes a random open move on the board
			move = tictactoe.chooseRandomMoveFromList(board, [1,2,3,4,5,6,7,8,9])
			tictactoe.makeMove(board, playerLetter, move)

			if tictactoe.isWinner(board, playerLetter):
				playerScore += 1
				gameIsPlaying = False
			else:
				if tictactoe.isBoardFull(board):
					ties += 1
					break
				else:
					turn = 'computer'

		if turn == 'computer':
			move = tictactoe.getComputerMove(board, computerLetter)
			tictactoe.makeMove(board, computerLetter, move)

			if tictactoe.isWinner(board, computerLetter):
				computerScore += 1
				gameIsPlaying = False
			else:
				if tictactoe.isBoardFull(board):
					ties += 1
					break
				else:
					turn = 'player'
print('Player wins:'+ str(playerScore) + ' Computer wins:'+ str(computerScore)+ ' Ties:'+ str(ties)+ ' NumberOfGamesPlayed:'+ str(numGamesPlayed))