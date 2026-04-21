class GameLogic:
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = True  # True - Cross, False - Circle

    @staticmethod
    def convert_coord_to_row_column(coord):
        """Translates cursor position into exact row or column. Then validates whether the cursor is inside playing board. """
        row_col = (coord // 100) - 1
        if row_col >= 3 or row_col < 0:
            return None
        else:
            return row_col

    def click_action(self, cursor_position):
        """Takes cursor position, translates it into exact row and column, and returns it with current player. """
        x_coord, y_coord = cursor_position
        row = self.convert_coord_to_row_column(y_coord)
        col = self.convert_coord_to_row_column(x_coord)

        if row is not None and col is not None:
            if self.board[row][col] is None:
                player = self.current_player
                self.board[row][col] = player
                self.switch_current_player()
            else:
                return None
            return row, col, player
        else:
            return None

    def switch_current_player(self):
        """Switches current player after the move is made. """
        self.current_player = not self.current_player

    def clear_board(self):
        """Wipes the board after every win or draw. """
        self.board = [[None for _ in range(3)] for _ in range(3)]

    def check_full_board(self):
        """Checks whether board is full (draw) in case there is no winners. """
        for row in self.board:
            if None in row:
                return False
        return True

    def check_win(self):
        """Checks whether 1 of 3 winning conditions are achieved. """
        for func in (self.check_win_rows(), self.check_win_columns(), self.check_win_diagonals()):
            result = func
            if result is not None:
                return result
        return None

    def check_win_rows(self):
        """Checks whether there are 3 the same symbols in row. """
        for row in self.board:
            if row[0] == row[1] == row[2] is not None:
                return row[0]
        return None

    def check_win_columns(self):
        """Checks whether there are 3 the same symbols in column. """
        for col in range(0, 3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] is not None:
                return self.board[0][col]
        return None

    def check_win_diagonals(self):
        """Checks whether there are 3 the same symbols in diagonals. """
        if ((self.board[0][0] == self.board[1][1] == self.board[2][2] is not None) or
                (self.board[0][2] == self.board[1][1] == self.board[2][0] is not None)):
            return self.board[1][1]
        return None
