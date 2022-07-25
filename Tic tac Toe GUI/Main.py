import sys, pygame
import random

## TBC check for darw and avoid none type at the end and check the strike through

pygame.init()

WIDTH = 600
HEIGHT = 600
BG_COLOR = (174,198,207)
BLACK = (0,0,0)

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(BG_COLOR)

def draw_lines():
    pygame.draw.line(screen, BLACK, (0,200),(600,200), width=10)
    pygame.draw.line(screen, BLACK, (0, 400), (600, 400), width=10)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 600), width=10)
    pygame.draw.line(screen, BLACK, (400, 0), (400, 600), width=10)

def draw_x(x_axis, y_axis):
    pygame.draw.line(screen, BLACK, (x_axis, y_axis), (x_axis + 100, y_axis + 100), width=10)
    pygame.draw.line(screen, BLACK, (x_axis, y_axis + 100), (x_axis+100, y_axis), width=10)

def draw_circ(x_co, y_co):
    pygame.draw.circle(screen, BLACK, (int(x_co * 200) + 100, int(y_co * 200) + 100), 50, 10)

def draw_win_str(y_pos):
    pygame.draw.line(screen, (255,0,0), (100, y_pos*200+100), (500, y_pos*200+100), width=5)

def draw_win_dwn(y_pos):
    pygame.draw.line(screen, (255, 0, 0), (y_pos * 200 + 100, 100), (y_pos * 200 + 100, 500), width=5)

def draw_win_desc():
    pygame.draw.line(screen, (255, 0, 0), (100, 100), (500, 500), width=5)

def draw_win_asc():
    pygame.draw.line(screen, (255, 0, 0), (500,100), (100,500), width=5)

draw_lines()

#pygame.draw.circle(screen, BLACK, (int(x_co*200)+100,int(y_co*200)+100), 50, 10)

def str_winner(board):
    if(board[0] == board[1] == board[2]):
        draw_win_str(0)

    elif(board[3] == board[4] == board[5]):
        draw_win_str(1)

    elif(board[6] == board[7] == board[8]):
        draw_win_str(2)

    elif(board[0] == board[3] == board[6]):
        draw_win_dwn(0)

    elif(board[1] == board[4] == board[7]):
        draw_win_dwn(1)

    elif(board[2] == board[5] == board[8]):
        draw_win_dwn(2)

    elif(board[0] == board[4] == board[8]):
        draw_win_desc()

    elif(board[2] == board[4] == board[6]):
        draw_win_asc()


def move(board, number, player):
    board[number - 1] = player

def show_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print('--+---+--')
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print('--+---+--')
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, player, ismain=False):
    if ((board[0] == board[1] == board[2] and board[0] == player) or
            (board[3] == board[4] == board[5] and board[3] == player) or
            (board[6] == board[7] == board[8] and board[6] == player)):
        if ismain:
            show_board(board)
            print(f"winner is {player}")
        return True
    elif ((board[0] == board[3] == board[6] and board[0] == player) or
          (board[1] == board[4] == board[7] and board[1] == player) or
          (board[2] == board[5] == board[8] and board[2] == player)):
        if ismain:
            show_board(board)
            print(f"winner is {player}")
        return True
    elif ((board[0] == board[4] == board[8] and board[0] == player) or
          (board[2] == board[4] == board[6] and board[6] == player)):
        if ismain:
            show_board(board)
            print(f"winner is {player}")
        return True
    else:
        return False

def check_for_draw(board):
    for x in board:
        if x != "X" and x != "O":
            return False
    return True

def minimax(board, ismaxima, i):
    if check_winner(board, "X"):
        return -100
    if check_winner(board, "O"):
        return 100
    if check_for_draw(board):
        return 0
    if ismaxima:
        high = -99
        for spots in board:
            if spots != "X" and spots != "O":
                board[spots - 1] = "O"
                val = minimax(board, False, i)
                board[spots - 1] = spots
                high = max(high, val)
        return high
    else:
        low = 99
        for spots in board:
            if spots != "X" and spots != "O":
                board[spots - 1] = "X"
                val = minimax(board, True, i)
                board[spots - 1] = spots
                low = min(low, val)
        return low

def botplay(board, i=0):
    best_score = -1000
    best_move = 0
    for x in board:
        if (x != "X" and x != "O"):
            board[x - 1] = "O"
            score = minimax(board, False, i)
            board[x - 1] = x
            if best_score < score:
                best_score = score
                best_move = x
    move(board, best_move, "O")

    refer = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
    }
    #if board[4] == 5:
    #    x_co = 1
    #    y_co = 1
    #    move(board, 5, "O")
    #else:
    x_co = refer.get(best_move)[1]
    y_co = refer.get(best_move)[0]

    show_board(board)
    pygame.draw.circle(screen, BLACK, (int(x_co * 200) + 100, int(y_co * 200) + 100), 50, 10)

def player_move(board, x_co, y_co):
    refer = {
        0:1,
        1:4,
        2:7
    }
    print(x_co, y_co)
    x_axis = int(x_co * 200) + 50
    y_axis = int(y_co * 200) + 50
    draw_x(x_axis, y_axis)
    position = refer.get(y_co)+x_co
    move(board, position, "X")
    show_board(board)

def bot_first_move(board):
    main = [1,3,7,9]
    rndm = random.randint(0,3)
    if board[4] == 5:
        return 4
    while(board[main[rndm]-1]=="X" or board[main[rndm]-1]=="X"):
        rndm = random.randint(0,3)
    return main[rndm]-1

'''
def tic_tac_toe():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(5):
        if check_winner(board, "X"):
            show_board(board)
            print("WINNER IS X")
            return
        if check_winner(board, "O"):
            show_board(board)
            print("WINNER IS O")
            return
        if i == 4:
            show_board(board)
            print("DRAW")
            return
        show_board(board)
        player_move(board)
        show_board(board)
        os.system('clear')
        print("\n")
        if i == 0:
            board[bot_first_move(board)] = "O"
        else:
            botplay(board)
'''

def restart():
    screen.fill(BG_COLOR)
    draw_lines()
    for x in range(1,10):
        board[x-1] = x

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_over = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and game_over is False:
            x_co = event.pos[0]//200
            y_co = event.pos[1]//200
            player_move(board, x_co, y_co)
            if check_for_draw(board):
                game_over=True
            elif check_winner(board, "X"):
                game_over = True
                str_winner(board)
            elif check_winner(board, "O"):
                game_over = True
                str_winner(board)
            if game_over is False:
                botplay(board)
                if check_winner(board, "X"):
                    game_over = True
                    str_winner(board)
                elif check_winner(board, "O"):
                    game_over = True
                    str_winner(board)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False

    pygame.display.update()
