import pygame
from files.constants import SQUARE_SIZE, WIDTH,HEIGHT,RED, BLUE
from files.board import Board
from files.game import Game
from minimax.algorithm import minimax
from alphabeta.algorithm import minimax_pruning

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Sholo Ghuti')

def get_row_col_from_mouse(pos):
    x , y = pos
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row,col 


def main():
    run = True
    clock = pygame.time.Clock()
    # board = Board()
    game = Game(WIN)

   
    while run:
        clock.tick(FPS)

        if game.turn == BLUE:
            value, new_board = minimax(game.get_board(),3,BLUE, game)
            #value, new_board = minimax_pruning(game.get_board(), 0,True, game, float('-inf'), float('inf'))
            game.ai_move(new_board)

        if game.winner()!= None:
            print(game.winner())
            run = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                print(f"row {row} col {col}")
                # piece = board.get_piece(row,col)
                # board.move(piece,4,3)
                # if game.turn == RED:
                game.select(row,col)

        # board.draw(WIN)
        # pygame.display.update()
        game.update()

    pygame.quit()

main()