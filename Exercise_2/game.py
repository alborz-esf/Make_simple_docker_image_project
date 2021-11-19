# A.Esfandyari
import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

# sign variable to decide the turn of which player
sign = 0

# Creates an empty board
global board
board = [[" " for x in range(3)] for y in range(3)]


# Check l(O/X) won the match or not
# according to the rules of the game
class game_:
    def winner(self, b, l):
        return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
                (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
                (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
                (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
                (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
                (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
                (b[0][0] == l and b[1][1] == l and b[2][2] == l) or
                (b[0][2] == l and b[1][1] == l and b[2][0] == l))

    # Configure text on button while playing with another player
    def get_text(self, i, j, gb, l1, l2):
        global sign
        if board[i][j] == ' ':
            if sign % 2 == 0:
                l1.config(state=DISABLED)
                l2.config(state=ACTIVE)
                board[i][j] = "X"
            else:
                l2.config(state=DISABLED)
                l1.config(state=ACTIVE)
                board[i][j] = "O"
            sign += 1
            button[i][j].config(text=board[i][j])
        if self.winner(board, "X"):
            gb.destroy()
            box = messagebox.showinfo("Winner", "Player 1 won the match")
        elif self.winner(board, "O"):
            gb.destroy()
            box = messagebox.showinfo("Winner", "Player 2 won the match")
        elif (self.isfull()):
            gb.destroy()
            box = messagebox.showinfo("Tie Game", "Tie Game")

    # Check if the player can push the button or not
    def isfree(self, i, j):
        return board[i][j] == " "

    # Check the board is full or not
    def isfull(self):
        flag = True
        for i in board:
            if (i.count(' ') > 0):
                flag = False
        return flag

    # Create the GUI of game board for play along with another player
    def gameboard_pl(self, game_board, l1, l2):
        global button
        button = []
        for i in range(3):
            m = 3 + i
            button.append(i)
            button[i] = []
            for j in range(3):
                n = j
                button[i].append(j)
                get_t = partial(self.get_text, i, j, game_board, l1, l2)
                button[i][j] = Button(
                    game_board, bd=5, command=get_t, height=4, width=8)
                button[i][j].grid(row=m, column=n)
        game_board.mainloop()

    # Decide the next move of system
    def pc(self):
        possiblemove = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == ' ':
                    possiblemove.append([i, j])
        move = []
        if possiblemove == []:
            return
        else:
            for let in ['O', 'X']:
                for i in possiblemove:
                    boardcopy = deepcopy(board)
                    boardcopy[i[0]][i[1]] = let
                    if self.winner(boardcopy, let):
                        return i
            corner = []
            for i in possiblemove:
                if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                    corner.append(i)
            if len(corner) > 0:
                move = random.randint(0, len(corner) - 1)
                return corner[move]
            edge = []
            for i in possiblemove:
                if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                    edge.append(i)
            if len(edge) > 0:
                move = random.randint(0, len(edge) - 1)
                return edge[move]

    # Configure text on button while playing with system
    def get_text_pc(self, i, j, gb, l1, l2):
        global sign
        if board[i][j] == ' ':
            if sign % 2 == 0:
                l1.config(state=DISABLED)
                l2.config(state=ACTIVE)
                board[i][j] = "X"
            else:
                button[i][j].config(state=ACTIVE)
                l2.config(state=DISABLED)
                l1.config(state=ACTIVE)
                board[i][j] = "O"
            sign += 1
            button[i][j].config(text=board[i][j])
        x = True
        if self.winner(board, "X"):
            gb.destroy()
            x = False
            box = messagebox.showinfo("Winner", "Player won the match")
        elif self.winner(board, "O"):
            gb.destroy()
            x = False
            box = messagebox.showinfo("Winner", "Computer won the match")
        elif (self.isfull()):
            gb.destroy()
            x = False
            box = messagebox.showinfo("Tie Game", "Tie Game")
        if (x):
            if sign % 2 != 0:
                move = self.pc()
                button[move[0]][move[1]].config(state=DISABLED)
                self.get_text_pc(move[0], move[1], gb, l1, l2)

    # Create the GUI of game board for play along with system
    def gameboard_pc(self, game_board, l1, l2):
        global button
        button = []
        for i in range(3):
            m = 3 + i
            button.append(i)
            button[i] = []
            for j in range(3):
                n = j
                button[i].append(j)
                get_t = partial(self.get_text_pc, i, j, game_board, l1, l2)
                button[i][j] = Button(
                    game_board, bd=5, command=get_t, height=4, width=8)
                button[i][j].grid(row=m, column=n)
        game_board.mainloop()

    # Initialize the game board to play with system
    def withpc(self, game_board):
        game_board.destroy()
        game_board = Tk()
        game_board.title("Tic Tac Toe")
        l1 = Button(game_board, text="Player : X", width=10)
        l1.grid(row=1, column=1)
        l2 = Button(game_board, text="Computer : O",
                    width=10, state=DISABLED)

        l2.grid(row=2, column=1)
        self.gameboard_pc(game_board, l1, l2)

    # Initialize the game board to play with another player
    def withplayer(self, game_board):
        self.game_board.destroy()
        game_board = Tk()
        game_board.title("Tic Tac Toe")
        l1 = Button(game_board, text="Player 1 : X", width=10)

        l1.grid(row=1, column=1)
        l2 = Button(game_board, text="Player 2 : O",
                    width=10, state=DISABLED)

        l2.grid(row=2, column=1)
        self.gameboard_pl(game_board, l1, l2)
