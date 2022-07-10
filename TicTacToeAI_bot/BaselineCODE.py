import os
import random


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
    for avail in board:
        if avail != "X" or avail != "O":
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


def player_move(board):
    position = int(input("WHERE WUD U LIKE TO PLACE X: "))
    move(board, position, "X")

def bot_first_move(board):
    main = [1,3,7,9]
    rndm = random.randint(0,3)
    while(board[main[rndm]-1]=="X" or board[main[rndm]-1]=="X"):
        rndm = random.randint(0,3)
    return main[rndm]-1



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

tic_tac_toe()
