# Python Chess Game

A simple command-line chess game for two players, written in Python.

## Features

- Complete chess board with all pieces
- All standard chess piece movements (King, Queen, Rook, Bishop, Knight, Pawn)
- Two-player gameplay
- Input validation
- Check and checkmate detection
- Stalemate detection
- Clean, object-oriented design

## Files

- `main.py` - Entry point for the game
- `board.py` - Board class that manages the chess board
- `square.py` - Square class representing each square on the board
- `piece.py` - Base Piece class and PieceColor enum
- `pieces.py` - All chess piece classes (King, Queen, Rook, Bishop, Knight, Pawn)
- `player.py` - Player class
- `game.py` - Game class that manages game logic and turns

## How to Run

1. Make sure you have Python 3.6 or higher installed
2. Navigate to the game directory
3. Run the game:

```bash
python main.py
```

Or on Unix/Linux/Mac:

```bash
python3 main.py
```

## How to Play

1. The board is displayed with coordinates (0-7 for both rows and columns)
2. White pieces start at rows 6-7, Black pieces at rows 0-1
3. Players take turns moving pieces
4. Enter coordinates as two numbers separated by a space:
   - First, enter the position of the piece you want to move (e.g., "6 0")
   - Then, enter the destination position (e.g., "5 0")

### Piece Symbols

- **K** = King
- **Q** = Queen
- **R** = Rook
- **B** = Bishop
- **N** = Knight
- **P** = Pawn
- **-** = Empty square

### Board Layout

```
  0 1 2 3 4 5 6 7
0 R N B Q K B N R  (Black pieces)
1 P P P P P P P P  (Black pawns)
2 - - - - - - - -
3 - - - - - - - -
4 - - - - - - - -
5 - - - - - - - -
6 P P P P P P P P  (White pawns)
7 R N B Q K B N R  (White pieces)
```

## Game Rules

- Players alternate turns (White goes first)
- Each piece moves according to standard chess rules
- You cannot move into check
- The game ends when a player is checkmated or stalemated

## Advantages of Python Version

Compared to the Java version, this Python implementation:
- Is more concise and readable
- No compilation needed - just run the script
- Easier to modify and extend
- Automatic memory management
- Built-in support for proper exception handling
- Uses Python's elegant syntax and features

## Example Gameplay

```
Enter the row and column of the piece you want to move (e.g., '2 3'): 6 4
Enter the row and column of the destination square (e.g., '4 5'): 4 4
```

This moves the white pawn from position (6,4) to (4,4).

## Requirements

- Python 3.6 or higher
- No external dependencies required!

Enjoy playing chess!
