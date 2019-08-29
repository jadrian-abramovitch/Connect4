import numpy as np
import pygame
import sys
import math

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)


def create_board():
	board = np.zeros((6,7))
	return board

def draw_board(board):
	for j in range (7):
		for i in range(6):
			pygame.draw.rect(screen, BLUE, (j*square_size, i*square_size+square_size, square_size, square_size))
			if board[i][j] == 0:
				pygame.draw.circle(screen, BLACK,(int(j*square_size+square_size/2), int(i*square_size+square_size+square_size/2)) ,radius)
			elif board[i][j] == 1:
				pygame.draw.circle(screen, RED,(int(j*square_size+square_size/2), int(i*square_size+square_size+square_size/2)) ,radius)
			elif board[i][j] == 2:
				pygame.draw.circle(screen, YELLOW,(int(j*square_size+square_size/2), int(i*square_size+square_size+square_size/2)) ,radius)
	pygame.display.update()

def drop_piece(board, row, col, player):
	board[row][col] = player
	return board

def is_valid_location(board, col):
	return board[0][col] == 0

def get_next_open_row(board, col):
	for i in range(5,-1,-1):
		if board[i][col] == 0:
			return i

def check_for_win(board, player):
	#check for horizontal win
	for j in range(4):
		for i in range(6):
			if board[i][j] == player and board[i][j+1] == player and board[i][j+2] == player and board[i][j+3] == player:
				return True

	#check for vertical win
	for i in range(3):
		for j in range(7):
			if board[i][j] == player and board[i+1][j] == player and board[i+2][j] == player and board[i+3][j] == player:
				return True	

	#check for downwards sloping diagonal win
	for i in range(3):
		for j in range(4):
			if board[i][j] == player and board[i+1][j+1] == player and board[i+2][j+2] == player and board[i+3][j+3] == player:
				return True			

	#check for upwards sloping diagonal win
	for i in range(3,6):
		for j in range(4):
			if board[i][j] == player and board[i-1][j+1] == player and board[i-2][j+2] == player and board[i-3][j+3] == player:
				return True			
	return False


board = create_board()
game_over = False
player = 1

pygame.init()

square_size = 100
width = 7 * square_size
height = 7 * square_size

size = (width, height)

radius = int(square_size/2 - 5)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 75)

while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, BLACK, (0,0, width, square_size))
			posx = event.pos[0]
			if player == 1:
				#pygame.draw.circle(screen, RED, (posx, int(square_size/2)), radius)
				pygame.draw.circle(screen, RED, (posx, 50), radius)
			else:
				pygame.draw.circle(screen, YELLOW, (posx, int(square_size/2)), radius)
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, BLACK, (0,0, width, square_size))

		#player 1 input
			if player == 1:
				posx = event.pos[0]
				selection = math.floor(posx/square_size)
			# 	selection = int(input("Player 1 Choose 0-6:"))

				if is_valid_location(board, selection):
					row = get_next_open_row(board, selection)
					board = drop_piece(board, row, selection, player)

					if check_for_win(board, player):
						label = myfont.render("Player 1 wins!", 1, RED)
						screen.blit(label, (40,10))
						print("Player 1 wins!")
						game_over = True


				player +=1

			else:
				posx = event.pos[0]
				selection = math.floor(posx/square_size)
				#selection = int(input("Player 2 Choose 0-6:"))
				
				if is_valid_location(board, selection):
					row = get_next_open_row(board, selection)
					board = drop_piece(board, row, selection, player)

					if check_for_win(board, player):
						label = myfont.render("Player 2 wins!", 1, YELLOW)
						screen.blit(label, (40,10))
						print("Player 2 wins!")
						game_over = True

				player -= 1
			print(board)
			draw_board(board)

			if game_over == True:
				pygame.time.wait(5000)		