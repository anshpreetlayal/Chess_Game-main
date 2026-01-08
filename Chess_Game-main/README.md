# Interactive Chess Game 🎯♟️

A beautiful, interactive chess game playable in your web browser! No installation required - just open and play!

![Chess Game](https://img.shields.io/badge/Version-1.0-blue)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)

## ✨ Features

### Web Version (Interactive)
- **Beautiful UI** - Modern, gradient design with smooth animations
- **Interactive Gameplay** - Click to select pieces and see valid moves highlighted
- **Visual Feedback** - Selected pieces and valid moves are clearly highlighted
- **Move History** - Track all moves made during the game
- **Captured Pieces** - See which pieces have been captured by each player
- **Undo Functionality** - Made a mistake? Undo your last move!
- **New Game** - Start fresh anytime with a single click
- **Responsive Design** - Works on desktop, tablet, and mobile devices
- **No Installation Required** - Just open in a browser and play!

### Python CLI Version
- Command-line interface for classic gameplay
- All standard chess rules implemented
- Input validation and error handling

## 🎮 How to Play

### Web Version (Recommended)

1. Simply open `index.html` in your web browser
2. The game starts with White's turn
3. Click on any white piece to see its valid moves
4. Click on a highlighted square to move your piece there

**Making Moves:**
- **Select a Piece**: Click on one of your pieces (highlighted squares show valid moves)
- **Move the Piece**: Click on a highlighted square to move your piece there
- **Capture**: Click on a highlighted enemy piece to capture it
- **Deselect**: Click on empty space or another piece to deselect

**Game Controls:**
- **New Game** - Reset the board and start over
- **Undo Move** - Take back your last move
- **Move History** - View all moves made in the current game
- **Captured Pieces** - See pieces captured by each player

### Python CLI Version

```bash
python main.py
```

Enter coordinates as two numbers (row column) when prompted.

## 📁 Project Structure

```
Chess_Game-main/
├── Web Version (Interactive):
│   ├── index.html          # Main HTML file
│   ├── style.css           # Styling and layout
│   └── chess.js            # Game logic and mechanics
│
└── Python CLI Version:
    ├── main.py         # Python CLI entry point
    ├── board.py        # Board management
    ├── pieces.py       # Piece definitions
    ├── piece.py        # Base piece class
    ├── square.py       # Square class
    ├── player.py       # Player class
    └── game.py         # Game logic
```

## 🎨 Visual Features (Web Version)

### Board
- Classic checkerboard pattern with beige and brown squares
- Row and column coordinates (a-h, 1-8)
- Smooth hover effects
- Professional shadow and border

### Pieces
- Beautiful Unicode chess symbols
- White pieces: ♔ ♕ ♖ ♗ ♘ ♙
- Black pieces: ♚ ♛ ♜ ♝ ♞ ♟
- Drop shadow for 3D effect

### Highlights
- **Green** - Selected piece
- **Yellow** - Valid move squares
- **Green dot** - Empty squares you can move to
- **Red circle** - Enemy pieces you can capture

## 🎯 Chess Rules Implemented

### Piece Movements

- **Pawn** ♙ - Moves forward one square (two on first move), captures diagonally
- **Rook** ♖ - Moves horizontally or vertically any number of squares
- **Knight** ♘ - Moves in L-shape (2+1 squares)
- **Bishop** ♗ - Moves diagonally any number of squares
- **Queen** ♕ - Combines rook and bishop movements
- **King** ♔ - Moves one square in any direction

### Game Mechanics

- Turn-based gameplay (White moves first)
- Piece capture
- Move validation
- Game over when king is captured

## 🚀 Quick Start

### Web Version (Recommended)

1. Navigate to the project folder
2. Double-click `index.html`
3. The game opens in your default browser
4. Start playing!

**Alternative**: Right-click `index.html` → Open with → Choose your browser

### Python CLI Version

```bash
python main.py
```

Or:

```bash
python3 main.py
```

## 💻 Browser Compatibility

Works with all modern browsers:
- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Opera

## 📱 Responsive Design

The game automatically adapts to your screen size:
- **Desktop**: Full-featured experience with large board
- **Tablet**: Optimized layout with touch support
- **Mobile**: Compact design that fits smaller screens

## 🛠️ Technical Details

### Technologies Used

- **HTML5** - Structure and semantics
- **CSS3** - Styling, animations, and gradients
- **Vanilla JavaScript** - Game logic (no frameworks!)
- **Python 3.6+** - CLI version with object-oriented design

### Key Features

- Object-oriented design
- Event-driven architecture
- Modular code structure
- Efficient move validation
- State management for undo functionality

## 📝 Future Enhancements

Planned features:
- [ ] Check and checkmate detection (advanced)
- [ ] Castling support
- [ ] En passant capture
- [ ] Pawn promotion
- [ ] Draw by repetition
- [ ] Save/load games
- [ ] AI opponent
- [ ] Timer/clock
- [ ] Sound effects
- [ ] Game analysis

## 🤝 Contributing

Contributions are welcome! If you'd like to improve the game by adding new features, improving existing functionalities, or fixing issues, feel free to fork the repository and create a pull request.



