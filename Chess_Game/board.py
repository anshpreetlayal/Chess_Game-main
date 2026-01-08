from square import Square
from pieces import King, Queen, Rook, Bishop, Knight, Pawn
from piece import PieceColor


class Board:
    def __init__(self, num_rows=8, num_cols=8):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.squares = [[None for _ in range(num_cols)] for _ in range(num_rows)]
        self.initialize_board()

    def initialize_board(self):
        # Initialize all squares as empty
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.squares[row][col] = Square(row, col, None)

        # Place black pieces (row 0 and 1)
        self.place_piece(Rook(PieceColor.BLACK, self.squares[0][0]), 0, 0)
        self.place_piece(Knight(PieceColor.BLACK, self.squares[0][1]), 0, 1)
        self.place_piece(Bishop(PieceColor.BLACK, self.squares[0][2]), 0, 2)
        self.place_piece(Queen(PieceColor.BLACK, self.squares[0][3]), 0, 3)
        self.place_piece(King(PieceColor.BLACK, self.squares[0][4], self), 0, 4)
        self.place_piece(Bishop(PieceColor.BLACK, self.squares[0][5]), 0, 5)
        self.place_piece(Knight(PieceColor.BLACK, self.squares[0][6]), 0, 6)
        self.place_piece(Rook(PieceColor.BLACK, self.squares[0][7]), 0, 7)

        # Place black pawns
        for col in range(8):
            self.place_piece(Pawn(PieceColor.BLACK, self.squares[1][col]), 1, col)

        # Place white pieces (row 7 and 6)
        self.place_piece(Rook(PieceColor.WHITE, self.squares[7][0]), 7, 0)
        self.place_piece(Knight(PieceColor.WHITE, self.squares[7][1]), 7, 1)
        self.place_piece(Bishop(PieceColor.WHITE, self.squares[7][2]), 7, 2)
        self.place_piece(Queen(PieceColor.WHITE, self.squares[7][3]), 7, 3)
        self.place_piece(King(PieceColor.WHITE, self.squares[7][4], self), 7, 4)
        self.place_piece(Bishop(PieceColor.WHITE, self.squares[7][5]), 7, 5)
        self.place_piece(Knight(PieceColor.WHITE, self.squares[7][6]), 7, 6)
        self.place_piece(Rook(PieceColor.WHITE, self.squares[7][7]), 7, 7)

        # Place white pawns
        for col in range(8):
            self.place_piece(Pawn(PieceColor.WHITE, self.squares[6][col]), 6, col)

    def get_square(self, row, col):
        if self.is_valid_position(row, col):
            return self.squares[row][col]
        return None

    def is_valid_position(self, row, col):
        return 0 <= row < self.num_rows and 0 <= col < self.num_cols

    def is_valid_square(self, row, col):
        return self.is_valid_position(row, col)

    def place_piece(self, piece, row, col):
        if self.is_valid_position(row, col):
            square = self.squares[row][col]
            square.set_piece(piece)
            piece.set_current_position(square)
        else:
            print("Invalid position for placing piece.")

    def remove_piece(self, row, col):
        if self.is_valid_position(row, col):
            self.squares[row][col].set_piece(None)
        else:
            print("Invalid position for removing piece.")

    def display_board(self):
        print("\n  0 1 2 3 4 5 6 7")
        for row in range(self.num_rows):
            print(f"{row} ", end="")
            for col in range(self.num_cols):
                piece = self.squares[row][col].get_piece()
                if piece is not None:
                    print(f"{piece.get_symbol()} ", end="")
                else:
                    print("- ", end="")
            print()
        print()

    def get_squares(self):
        return self.squares

    def get_num_rows(self):
        return self.num_rows

    def get_num_cols(self):
        return self.num_cols
