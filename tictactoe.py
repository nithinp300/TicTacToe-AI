import random

def drawBoard(board):
	# "board" is a list of 10 strings representing the board (ignore index 0)
	print('     |     |')
	print('  ' + board[7] + '  |  ' + board[8] + '  |  ' + board[9])
	print('     |     |')
	print('----------------')
	print('     |     |')
	print('  ' + board[4] + '  |  ' + board[5] + '  |  ' + board[6])
	print('     |     |')
	print('----------------')
	print('     |     |')
	print('  ' + board[1] + '  |  ' + board[2] + '  |  ' + board[3])
	print('     |     |')

def inputPlayerLetter():
	letter = 'X'
	while not(letter == 'X' or letter == 'O'):
		letter = input('Do you want to be X or O? ').upper()

	# the first element in the list is the player’s letter, the second is the computer's letter.
	if letter == 'X':
		return ['X', 'O']
	else:
		return ['O', 'X']

def whoGoesFirst():
	# Randomly choose the player who goes first.
	if random.randint(0, 1) == 0:
		return 'computer'
	else:
		return 'player'

def playAgain():
	# This function returns True if the player wants to play again, otherwise it returns False.
	return input('Do you want to play again?(y or n) ').lower().startswith('y')

def isWinner(bo, le):
	return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
	(bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
	(bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
	(bo[7] == le and bo[4] == le and bo[1] == le) or # down the left
	(bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
	(bo[9] == le and bo[6] == le and bo[3] == le) or # down the right
	(bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
	(bo[9] == le and bo[5] == le and bo[1] == le))   # diagonal

def getBoardCopy(board):
	# Make a duplicate of the board list and return it the duplicate.
	duplicateBoard = []
	for i in board:
		duplicateBoard.append(i)
	return duplicateBoard

def isSpaceFree(board, move):
	return board[move] == ' '

def makeMove(board, letter, move):
	board[move] = letter

def getPlayerMove(board):
	# Let the player type in their move.
	move = ''
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
		move = input('What is your next move? (1-9) ')
	return int(move)

def chooseRandomMoveFromList(board, movesList):
	# Returns a valid move from the passed list on the passed board
	# return none if there is no valid move
	possibleMoves = []
	for i in movesList:
		if isSpaceFree(board, i):
			possibleMoves.append(i)
	if(len(possibleMoves) != 0):
		return random.choice(possibleMoves)
	else:
		return None

def isForkMove(board, letter, move):
	# we check if a move creates a fork
	copy = getBoardCopy(board)
	makeMove(copy, letter, move)
	winningMoves = 0
	for i  in range(1, 10):
		if isSpaceFree(copy, i) and testWinMove(copy, letter, i):
			winningMoves += 1
	return winningMoves >= 2

def testWinMove(board, letter, move):
	copy = getBoardCopy(board)
	copy[move] = letter
	return isWinner(copy, letter)

def getComputerMove(board, computerLetter):
	# Given a board and the computer's letter, we determine where to move and return that move.
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	# Tic Tac Toe AI Algorithm
	# 1) We check if we can win in the next move
	for i in range(1, 10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, computerLetter, i)
			if isWinner(copy, computerLetter):
				return i

	# 2) We check if there is a move the player can make that will cause computer to lose game.
	# If there is, the computer should move there to block the player.
	for i in range(1, 10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, playerLetter, i)
			if isWinner(copy, playerLetter):
				return i

	# 3) We check computer forks
	for i in range(1, 10):
		if isSpaceFree(board, i) and isForkMove(board, computerLetter, i):
			return i

	# 4) We check player forks
	playerForks = 0
	tempMove = None
	for i in range(1, 10):
		if isSpaceFree(board, i) and isForkMove(board, playerLetter, i):
			playerForks += 1
			tempMove = i
	if playerForks == 1:
		return tempMove
	elif playerForks == 2:
		return chooseRandomMoveFromList(board, [2, 4, 6, 8])

	# 5) We check if the center space is free.
	if isSpaceFree(board, 5):
		return 5

	# 6) We check if any of the corner spaces are free.
	move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
	if move != None:
		return move

	# 7) Lastly, we choose randomly any of the side spaces that are free
	return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
	for i in range(1, 10):
		if isSpaceFree(board, i):
			return False
	return True
