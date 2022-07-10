import telebot
import telegram
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

#API KEY HIDDEN FOR OBVIOUS REASONS
updater = Updater('API_KEY', use_context=True)

board = [1,2,3,4,5,6,7,8,9]


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Hello, Welcome to the Tic Tac Toe Bot. Please click on\n"
		"/help to see the commands available.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text(
		f"-------------RULES----------------\n"
		"\n"
		f"1.) You will play as X and the bot will play as O\n"
		"\n"
		f"2.) click on the respective number to slot the X into position\n"
		"\n"
		f"3.) after your turn click on the /botplay button that appears to allow the computer to play\n"
		"\n"
		f"4.) click on /begin to start the game and type /restart in case u want to reset from the beginning")


slash = ["/"]*9

def begin(update: Update, context: CallbackContext):
	for x in range(10):
		board[x-1] = x
	slash = ["/"]*9
	update.message.reply_text(f"{slash[0]}{board[0]}  |{slash[1]}{board[1]}    |{slash[2]}{board[2]}\n" 
							  f"--+---+--\n"
							  f"{slash[3]}{board[3]}  |{slash[4]}{board[4]}   |{slash[5]}{board[5]}\n"
							  f"--+---+--\n"
							  f"{slash[6]}{board[6]}  |{slash[7]}{board[7]}    |{slash[8]}{board[8]}\n")


def one(update: Update, context: CallbackContext):
	board[0] = "X"
	slash[0] = " "
	update.message.reply_text(f"{board[0]}  | {board[1]}    | {board[2]}\n" 
							  f"--+---+--\n"
							  f"{board[3]}  |{ board[4]}   | {board[5]}\n"
							  f"--+---+--\n"
							  f"{board[6]}  | {board[7]}    | {board[8]}\n"
							  "\n"
							  f"/botplay")

	if check_win(board, "X"):
		update.message.reply_text(
			f"YOU hav won the game\n"
			f"click on /new to begin a new game"
		)
	if check_draw(board):
		update.message.reply_text(
			f"The Game has end in a DRAW\n"
			f"click on /new to begin a new game"
			)

def two(update: Update, context: CallbackContext):
	board[1] = "X"
	slash[1] = " "
	update.message.reply_text(f"{board[0]}  | {board[1]}    | {board[2]}\n" 
							  f"--+---+--\n"
							  f"{board[3]}  |{ board[4]}   | {board[5]}\n"
							  f"--+---+--\n"
							  f"{board[6]}  | {board[7]}    | {board[8]}\n"
							  "\n"
							  f"/botplay")
	if check_win(board, "X"):
		update.message.reply_text(
			f"YOU have won the game\n"
			f"click on /new to begin a new game"
		)
	if check_draw(board):
		update.message.reply_text(
			f"The Game has end in a DRAW\n"
			f"click on /new to begin a new game"
			)

def three(update: Update, context: CallbackContext):
	board[2] = "X"
	slash[2] = " "
	update.message.reply_text(f"{board[0]}  | {board[1]}    | {board[2]}\n" 
							  f"--+---+--\n"
							  f"{board[3]}  |{ board[4]}   | {board[5]}\n"
							  f"--+---+--\n"
							  f"{board[6]}  | {board[7]}    | {board[8]}\n"
							  "\n"
							  f"/botplay")
	if check_win(board, "X"):
		update.message.reply_text(
			f"YOU have won the game\n"
			f"click on /new to begin a new game"
		)
	if check_draw(board):
		update.message.reply_text(
			f"The Game has end in a DRAW\n"
			f"click on /new to begin a new game"
			)

def four(update: Update, context: CallbackContext):
	board[3] = "X"
	slash[3] = " "
	update.message.reply_text(f"{board[0]}  | {board[1]}    | {board[2]}\n" 
							  f"--+---+--\n"
							  f"{board[3]}  |{ board[4]}   | {board[5]}\n"
							  f"--+---+--\n"
							  f"{board[6]}  | {board[7]}    | {board[8]}\n"
							  "\n"
							  f"/botplay")
	if check_win(board, "X"):
		update.message.reply_text(
			f"YOU have won the game\n"
			f"click on /new to begin a new game"
		)
	if check_draw(board):
		update.message.reply_text(
			f"The Game has end in a DRAW\n"
			f"click on /new to begin a new game"
			)

def five(update: Update, context: CallbackContext):
	board[4] = "X"
	slash[4] = " "
	update.message.reply_text(f"{board[0]}  | {board[1]}    | {board[2]}\n" 
							  f"--+---+--\n"
							  f"{board[3]}  |{ board[4]}   | {board[5]}\n"
							  f"--+---+--\n"
							  f"{board[6]}  | {board[7]}    | {board[8]}\n"
							  "\n"
							  f"/botplay")
	if check_win(board, "X"):
		update.message.reply_text(
			f"YOU have won the game\n"
			f"click on /new to begin a new game"
		)
	if check_draw(board):
		update.message.reply_text(
			f"The Game has end in a DRAW\n"
			f"click on /new to begin a new game"
			)

def six(update: Update, context: CallbackContext):
	board[5] = "X"
	slash[5] = " "
	update.message.reply_text(f"{board[0]}  | {board[1]}    | {board[2]}\n" 
							  f"--+---+--\n"
							  f"{board[3]}  |{ board[4]}   | {board[5]}\n"
							  f"--+---+--\n"
							  f"{board[6]}  | {board[7]}    | {board[8]}\n"
							  "\n"
							  f"/botplay")
	if check_win(board, "X"):
		update.message.reply_text(
			f"YOU have won the game\n"
			f"click on /new to begin a new game"
		)
	if check_draw(board):
		update.message.reply_text(
			f"The Game has end in a DRAW\n"
			f"click on /new to begin a new game"
			)

def seven(update: Update, context: CallbackContext):
	board[6] = "X"
	slash[6] = " "
	update.message.reply_text(f"{board[0]}  | {board[1]}    | {board[2]}\n" 
							  f"--+---+--\n"
							  f"{board[3]}  |{ board[4]}   | {board[5]}\n"
							  f"--+---+--\n"
							  f"{board[6]}  | {board[7]}    | {board[8]}\n"
							  "\n"
							  f"/botplay")
	if check_win(board, "X"):
		update.message.reply_text(
			f"YOU have won the game\n"
			f"click on /new to begin a new game"
		)
	if check_draw(board):
		update.message.reply_text(
			f"The Game has end in a DRAW\n"
			f"click on /new to begin a new game"
			)

def eight(update: Update, context: CallbackContext):
	board[7] = "X"
	slash[7] = " "
	update.message.reply_text(f"{board[0]}  | {board[1]}    | {board[2]}\n" 
							  f"--+---+--\n"
							  f"{board[3]}  |{ board[4]}   | {board[5]}\n"
							  f"--+---+--\n"
							  f"{board[6]}  | {board[7]}    | {board[8]}\n"
							  "\n"
							  f"/botplay")
	if check_win(board, "X"):
		update.message.reply_text(
			f"YOU have won the game\n"
			f"click on /new to begin a new game"
		)
	if check_draw(board):
		update.message.reply_text(
			f"The Game has end in a DRAW\n"
			f"click on /new to begin a new game"
			)

def nine(update: Update, context: CallbackContext):
	board[8] = "X"
	slash[8] = " "
	update.message.reply_text(f"{board[0]}  | {board[1]}    | {board[2]}\n" 
							  f"--+---+--\n"
							  f"{board[3]}  |{ board[4]}   | {board[5]}\n"
							  f"--+---+--\n"
							  f"{board[6]}  | {board[7]}    | {board[8]}\n"
							  "\n"
							  f"/botplay")
	if check_win(board, "X"):
		update.message.reply_text(
			f"YOU have won the game\n"
			f"click on /new to begin a new game"
		)
	if check_draw(board):
		update.message.reply_text(
			f"The Game has end in a DRAW\n"
			f"click on /new to begin a new game"
			)

def bot_plays(update: Update, context: CallbackContext):
	botplay(board)
	update.message.reply_text(f"{slash[0]}{board[0]}  |{slash[1]}{board[1]}    |{slash[2]}{board[2]}\n" 
							  f"--+---+--\n"
							  f"{slash[3]}{board[3]}  |{slash[4]}{board[4]}   |{slash[5]}{board[5]}\n"
							  f"--+---+--\n"
							  f"{slash[6]}{board[6]}  |{slash[7]}{board[7]}    |{slash[8]}{board[8]}\n"
							  "\n")
	if check_win(board, "O"):
		update.message.reply_text(
			f"COMPUTER has WON the game\n"
			f"click on /new to begin a new game"
		)
	if check_draw(board):
		update.message.reply_text(
			f"The Game has ended in a DRAW\n"
			f"click on /new to begin a new game"
			)

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)

def check_draw(board):
	for x in board:
		if x != "X" and x != "O":
			return False
	return True


def check_win(board, player):
	if ((board[0] == board[1] == board[2] and board[0] == player) or
			(board[3] == board[4] == board[5] and board[3] == player) or
			(board[6] == board[7] == board[8] and board[6] == player)):
		return True
	elif ((board[0] == board[3] == board[6] and board[0] == player) or
		  (board[1] == board[4] == board[7] and board[1] == player) or
		  (board[2] == board[5] == board[8] and board[2] == player)):
		return True
	elif ((board[0] == board[4] == board[8] and board[0] == player) or
		  (board[2] == board[4] == board[6] and board[6] == player)):
		return True
	else:
		return False

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('new', begin))
updater.dispatcher.add_handler(CommandHandler('begin', begin))
updater.dispatcher.add_handler(CommandHandler('restart', begin))
updater.dispatcher.add_handler(CommandHandler('1', one))
updater.dispatcher.add_handler(CommandHandler('2', two))
updater.dispatcher.add_handler(CommandHandler('3', three))
updater.dispatcher.add_handler(CommandHandler('4', four))
updater.dispatcher.add_handler(CommandHandler('5', five))
updater.dispatcher.add_handler(CommandHandler('6', six))
updater.dispatcher.add_handler(CommandHandler('7', seven))
updater.dispatcher.add_handler(CommandHandler('8', eight))
updater.dispatcher.add_handler(CommandHandler('9', nine))
updater.dispatcher.add_handler(CommandHandler('botplay', bot_plays))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	Filters.command, unknown)) # Filters out unknown commands

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()


def move(board, number, player):
	board[number - 1] = player


def show_board(board):
	print(f"/{board[0]} | /{board[1]} | /{board[2]}")
	print('--+---+--')
	print(f"/{board[3]} | /{board[4]} | /{board[5]}")
	print('--+---+--')
	print(f"/{board[6]} | /{board[7]} | /{board[8]}")


def check_winner(board, player,ismain=False):
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


def botplay(board, i=0):
	best_score = -1000
	best_move = 0
	for x in board:
		if x != "X" and x != "O":
			board[x - 1] = "O"
			score = minimax(board, False, i)
			board[x - 1] = x
			if best_score < score:
				best_score = score
				best_move = x
	move(board, best_move, "O")
	slash[best_move-1] = " "


def minimax(board, ismaxima, i):
	if check_winner(board, "X"):
		return -100
	if check_winner(board, "O"):
		return 100
	if i == 9:
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

