from enum import Enum
from abc import ABC, abstractmethod


class PieceColor(Enum):
    WHITE = "WHITE"
    BLACK = "BLACK"


class Piece(ABC):
    def __init__(self, color, current_position=None):
        self.color = color
        self.current_position = current_position
        self.is_killed = False

    def get_color(self):
        return self.color

    def set_current_position(self, new_position):
        self.current_position = new_position

    def get_current_position(self):
        return self.current_position

    def is_white(self):
        return self.color == PieceColor.WHITE

    def is_killed_piece(self):
        return self.is_killed

    def set_killed(self, killed):
        self.is_killed = killed

    def can_move(self, board, start, end):
        """Check if the piece can move from start to end square."""
        # Check if the destination square is occupied by own piece
        if end.get_piece() is not None and end.get_piece().is_white() == self.is_white():
            return False

        # Check if the move is within the board boundaries
        if not board.is_valid_square(end.row, end.col):
            return False

        return True

    @abstractmethod
    def is_valid_move(self, destination):
        """Check if the move is valid for this piece type."""
        pass

    @abstractmethod
    def get_symbol(self):
        """Return the symbol representing this piece."""
        pass
