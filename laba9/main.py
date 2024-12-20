import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Крестики-нолики")
        self.window.geometry("400x450")
        self.window.resizable(False, False)
        self.center_window()
        self.board = [' ' for _ in range(9)]
        self.human_player = "X"
        self.bot_player = "O"
        self.current_player = self.human_player
        self.create_widgets()
        self.window.mainloop()

    def center_window(self):
        window_width = 400
        window_height = 450
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def create_widgets(self):
        self.buttons = []
        for i in range(9):
            button = tk.Button(self.window, text=' ', font=('Arial', 24), height=2, width=5,
                               command=lambda idx=i: self.make_move(idx))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        self.status_label = tk.Label(self.window, text="Ваш ход!", font=("Arial", 16))
        self.status_label.grid(row=3, column=0, columnspan=3)

        self.choice_label = tk.Label(self.window, text="Выберите свою фигуру:", font=("Arial", 12))
        self.choice_label.grid(row=4, column=0, columnspan=3)

        self.x_button = tk.Button(self.window, text="X", font=("Arial", 12), command=lambda: self.set_player("X"))
        self.x_button.grid(row=5, column=0)

        self.o_button = tk.Button(self.window, text="O", font=("Arial", 12), command=lambda: self.set_player("O"))
        self.o_button.grid(row=5, column=2)

    def set_player(self, choice):
        self.human_player = choice
        self.bot_player = "O" if choice == "X" else "X"
        self.current_player = self.human_player
        self.choice_label.destroy()
        self.x_button.destroy()
        self.o_button.destroy()

    def make_move(self, idx):
        if self.board[idx] == ' ' and self.current_player == self.human_player:
            self.board[idx] = self.human_player
            self.buttons[idx].config(text=self.human_player)
            if self.check_winner(self.human_player):
                self.status_label.config(text="Вы выиграли!")
                messagebox.showinfo("Победа", "Вы выиграли!")
                self.reset_game()
                return
            elif ' ' not in self.board:
                self.status_label.config(text="Ничья!")
                messagebox.showinfo("Ничья", "Ничья!")
                self.reset_game()
                return
            else:
                self.current_player = self.bot_player
                self.bot_move()

    def bot_move(self):
        best_score = -float('inf')
        best_move = None

        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = self.bot_player
                score = self.minimax(False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i

        if best_move is not None:
            self.board[best_move] = self.bot_player
            self.buttons[best_move].config(text=self.bot_player)
            if self.check_winner(self.bot_player):
                self.status_label.config(text="Бот выиграл!")
                messagebox.showinfo("Проигрыш", "Бот выиграл!")
                self.reset_game()
                return
            elif ' ' not in self.board:
                self.status_label.config(text="Ничья!")
                messagebox.showinfo("Ничья", "Ничья!")
                self.reset_game()
                return

        self.current_player = self.human_player
        self.status_label.config(text="Ваш ход!")

    def minimax(self, is_maximizing):
        if self.check_winner(self.bot_player):
            return 1
        if self.check_winner(self.human_player):
            return -1
        if ' ' not in self.board:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = self.bot_player
                    score = self.minimax(False)
                    self.board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = self.human_player
                    score = self.minimax(True)
                    self.board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self, player):
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in win_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        for button in self.buttons:
            button.config(text=' ')
        self.current_player = self.human_player
        self.status_label.config(text="Ваш ход!")


TicTacToe()

