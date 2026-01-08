from piece import Piece, PieceColor


class King(Piece):
    def __init__(self, color, current_position=None, board=None):
        super().__init__(color, current_position)
        self.castling_done = False
        self.board = board

    def is_valid_move(self, destination):
        row_diff = abs(destination.get_row() - self.current_position.get_row())
        col_diff = abs(destination.get_col() - self.current_position.get_col())
        # King can move one square in any direction
        return row_diff <= 1 and col_diff <= 1

    def can_move(self, board, start, end):
        if not self.is_valid_move(end):
            return False

        if end.get_piece() is not None and end.get_piece().get_color() == self.get_color():
            return False

        row_diff = abs(end.get_row() - start.get_row())
        col_diff = abs(end.get_col() - start.get_col())

        if row_diff > 1 or col_diff > 1:
            return False

        return True

    def get_symbol(self):
        return "K"


class Queen(Piece):
    def __init__(self, color, current_position=None):
        super().__init__(color, current_position)

    def is_valid_move(self, destination):
        row_diff = abs(destination.get_row() - self.current_position.get_row())
        col_diff = abs(destination.get_col() - self.current_position.get_col())
        # Queen can move horizontally, vertically, or diagonally
        return row_diff == 0 or col_diff == 0 or row_diff == col_diff

    def can_move(self, board, start, end):
        if not self.is_valid_move(end):
            return False

        # Check if there are no pieces in the path
        row_direction = 1 if end.get_row() > start.get_row() else (-1 if end.get_row() < start.get_row() else 0)
        col_direction = 1 if end.get_col() > start.get_col() else (-1 if end.get_col() < start.get_col() else 0)

        current_row = start.get_row() + row_direction
        current_col = start.get_col() + col_direction

        while current_row != end.get_row() or current_col != end.get_col():
            if board.get_square(current_row, current_col).get_piece() is not None:
                return False
            current_row += row_direction
            current_col += col_direction

        return True

    def get_symbol(self):
        return "Q"


class Rook(Piece):
    def __init__(self, color, current_position=None):
        super().__init__(color, current_position)

    def is_valid_move(self, destination):
        row_diff = abs(destination.get_row() - self.current_position.get_row())
        col_diff = abs(destination.get_col() - self.current_position.get_col())
        # Rook can move horizontally or vertically
        return (row_diff == 0 and col_diff > 0) or (row_diff > 0 and col_diff == 0)

    def can_move(self, board, start, end):
        if not self.is_valid_move(end):
            return False

        # Check if there are no pieces in the path
        if end.get_row() == start.get_row():
            # Moving horizontally
            col_direction = 1 if end.get_col() > start.get_col() else -1
            current_col = start.get_col() + col_direction

            while current_col != end.get_col():
                if board.get_square(start.get_row(), current_col).get_piece() is not None:
                    return False
                current_col += col_direction
        elif end.get_col() == start.get_col():
            # Moving vertically
            row_direction = 1 if end.get_row() > start.get_row() else -1
            current_row = start.get_row() + row_direction

            while current_row != end.get_row():
                if board.get_square(current_row, start.get_col()).get_piece() is not None:
                    return False
                current_row += row_direction
        else:
            return False

        return True

    def get_symbol(self):
        return "R"


class Bishop(Piece):
    def __init__(self, color, current_position=None):
        super().__init__(color, current_position)

    def is_valid_move(self, destination):
        row_diff = abs(destination.get_row() - self.current_position.get_row())
        col_diff = abs(destination.get_col() - self.current_position.get_col())
        # Bishop can move diagonally
        return row_diff == col_diff

    def can_move(self, board, start, end):
        if not self.is_valid_move(end):
            return False

        # Check if there are no pieces in the path
        row_direction = 1 if end.get_row() > start.get_row() else -1
        col_direction = 1 if end.get_col() > start.get_col() else -1

        current_row = start.get_row() + row_direction
        current_col = start.get_col() + col_direction

        while current_row != end.get_row() or current_col != end.get_col():
            if board.get_square(current_row, current_col).get_piece() is not None:
                return False
            current_row += row_direction
            current_col += col_direction

        return True

    def get_symbol(self):
        return "B"


class Knight(Piece):
    def __init__(self, color, current_position=None):
        super().__init__(color, current_position)

    def is_valid_move(self, destination):
        row_diff = abs(destination.get_row() - self.current_position.get_row())
        col_diff = abs(destination.get_col() - self.current_position.get_col())
        # Knight moves in L-shape
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)

    def can_move(self, board, start, end):
        return self.is_valid_move(end) and (
            end.get_piece() is None or end.get_piece().is_white() != self.is_white()
        )

    def get_symbol(self):
        return "N"


class Pawn(Piece):
    def __init__(self, color, current_position=None):
        super().__init__(color, current_position)

    def is_valid_move(self, destination):
        row_diff = destination.get_row() - self.current_position.get_row()
        col_diff = abs(destination.get_col() - self.current_position.get_col())

        # Pawn can move forward by one square or diagonally to capture
        if self.get_color() == PieceColor.WHITE:
            return (row_diff == -1 and col_diff == 0) or (row_diff == -1 and col_diff == 1)
        else:
            return (row_diff == 1 and col_diff == 0) or (row_diff == 1 and col_diff == 1)

    def can_move(self, board, start, end):
        if not self.is_valid_move(end):
            return False

        if end.get_piece() is not None and end.get_piece().is_white() == self.is_white():
            return False

        row_diff = abs(end.get_row() - start.get_row())
        col_diff = abs(end.get_col() - start.get_col())

        # Normal move: one square forward
        if row_diff == 1 and col_diff == 0:
            return end.get_piece() is None

        # Double-step on first move
        elif row_diff == 2 and col_diff == 0:
            if self.is_white() and start.get_row() == 6 and end.get_row() == 4:
                return (
                    board.get_square(5, start.get_col()).get_piece() is None
                    and end.get_piece() is None
                )
            elif not self.is_white() and start.get_row() == 1 and end.get_row() == 3:
                return (
                    board.get_square(2, start.get_col()).get_piece() is None
                    and end.get_piece() is None
                )

        # Diagonal capture
        elif row_diff == 1 and col_diff == 1:
            if end.get_piece() is not None:
                return True

        return False

    def get_symbol(self):
        return "P"
