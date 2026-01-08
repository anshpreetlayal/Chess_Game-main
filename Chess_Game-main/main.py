#!/usr/bin/env python3
"""
Chess Game - Main Entry Point
A simple command-line chess game for two players.
"""

from board import Board
from player import Player
from game import Game
from piece import PieceColor


def main():
    """Main function to start the chess game."""
    print("=" * 40)
    print("Welcome to Chess Game!")
    print("=" * 40)

    # Create the chess board
    board = Board(8, 8)

    # Create players
    player1 = Player("Player 1 (White)", PieceColor.WHITE)
    player2 = Player("Player 2 (Black)", PieceColor.BLACK)

    # Create and start the game
    game = Game(board, player1, player2)
    game.start_game()


if __name__ == "__main__":
    main()
