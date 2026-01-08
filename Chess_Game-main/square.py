class Square:
    def __init__(self, row, col, piece=None):
        self.row = row
        self.col = col
        self.piece = piece

    def get_piece(self):
        return self.piece

    def set_piece(self, piece):
        self.piece = piece
        if piece is not None:
            piece.set_current_position(self)

    def get_row(self):
        return self.row

    def get_col(self):
        return self.col
