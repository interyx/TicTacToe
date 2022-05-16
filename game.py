import time
import constant
from player import HumanPlayer, RandomComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(constant.ROWS * constant.COLS)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i*constant.ROWS:(i+1)*constant.COLS] for i in range(constant.ROWS)]:
            print ('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        number_board = [[str(i) for i in range(j*constant.ROWS, (j+1)*constant.COLS)] for j in range(constant.ROWS)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // constant.ROWS
        row = self.board[row_ind * constant.ROWS: (row_ind + 1) * constant.COLS]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * constant.COLS] for i in range(constant.COLS)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in constant.DIAGONAL1]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in constant.DIAGONAL2]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = constant.X
    while(game.empty_squares()):
        if letter == constant.O:
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

        if game.current_winner:
            if print_game:
                print(letter + ' wins!')
            return letter


        letter = constant.O if letter == constant.X else constant.X

    if print_game:
        print('It\'s a tie!')

    time.sleep(0.8)

if __name__ == '__main__':
    x_player = HumanPlayer(constant.X)
    o_player = RandomComputerPlayer(constant.O)
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)