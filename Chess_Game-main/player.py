from piece import PieceColor


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def is_white(self):
        return self.color == PieceColor.WHITE
