from pieces import King


class Game:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def start_game(self):
        print("Chess Game Started!")
        self.play_game()

    def play_game(self):
        while not self.is_game_over():
            self.display_board()
            self.take_turn()
            self.switch_player()

        self.display_result()

    def take_turn(self):
        while True:
            print(f"{self.current_player.get_name()}'s turn:")

            try:
                start_input = input("Enter the row and column of the piece you want to move (e.g., '2 3'): ")
                start_row, start_col = map(int, start_input.split())

                if not (0 <= start_row < 8 and 0 <= start_col < 8):
                    print("Invalid coordinates. Please enter values between 0 and 7.")
                    continue

                start_square = self.board.get_square(start_row, start_col)

                if not self.is_valid_piece(start_square):
                    print("Invalid piece or not your turn. Please try again.")
                    continue

                end_input = input("Enter the row and column of the destination square (e.g., '4 5'): ")
                end_row, end_col = map(int, end_input.split())

                if not (0 <= end_row < 8 and 0 <= end_col < 8):
                    print("Invalid coordinates. Please enter values between 0 and 7.")
                    continue

                end_square = self.board.get_square(end_row, end_col)

                if end_square is None or not start_square.get_piece().can_move(self.board, start_square, end_square):
                    print("Invalid move. Please try again.")
                    continue

                # Perform the move
                piece = start_square.get_piece()
                end_square.set_piece(piece)
                start_square.set_piece(None)
                piece.set_current_position(end_square)
                break

            except (ValueError, AttributeError):
                print("Invalid input. Please enter two numbers separated by a space.")
                continue

    def is_valid_piece(self, start_square):
        return (
            start_square is not None
            and start_square.get_piece() is not None
            and start_square.get_piece().is_white() == self.current_player.is_white()
        )

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def is_game_over(self):
        return self.is_checkmate(self.player1) or self.is_checkmate(self.player2) or \
               self.is_stalemate(self.player1) or self.is_stalemate(self.player2)

    def is_checkmate(self, player):
        king = self.find_king(player.is_white())
        if king is not None and self.is_in_check(king, player):
            return not self.has_legal_moves(king, player)
        return False

    def is_stalemate(self, player):
        for row in self.board.get_squares():
            for square in row:
                piece = square.get_piece()
                if piece is not None and piece.is_white() == player.is_white() and self.has_legal_moves(piece, player):
                    return False
        return True

    def is_in_check(self, piece, player):
        opponent_is_white = not player.is_white()
        squares = self.board.get_squares()

        for row in squares:
            for square in row:
                attacker = square.get_piece()
                if attacker is not None and attacker.is_white() == opponent_is_white and \
                   attacker.can_move(self.board, square, piece.get_current_position()):
                    return True
        return False

    def has_legal_moves(self, piece, player):
        squares = self.board.get_squares()

        for row in squares:
            for square in row:
                if piece.can_move(self.board, piece.get_current_position(), square):
                    # Simulate the move
                    current_piece = square.get_piece()
                    square.set_piece(piece)
                    piece.get_current_position().set_piece(None)

                    legal_move = not self.is_in_check(self.find_king(player.is_white()), player)

                    # Undo the move
                    square.set_piece(current_piece)
                    piece.get_current_position().set_piece(piece)

                    if legal_move:
                        return True
        return False

    def find_king(self, is_white):
        for row in range(8):
            for col in range(8):
                square = self.board.get_square(row, col)
                piece = square.get_piece()
                if isinstance(piece, King) and piece.is_white() == is_white:
                    return piece
        return None

    def display_board(self):
        self.board.display_board()

    def display_result(self):
        if self.is_checkmate(self.player1):
            print("Player 1 is in checkmate. Player 2 wins!")
        elif self.is_checkmate(self.player2):
            print("Player 2 is in checkmate. Player 1 wins!")
        elif self.is_stalemate(self.player1) or self.is_stalemate(self.player2):
            print("Stalemate! The game is a draw.")
        else:
            print("Game Over!")
