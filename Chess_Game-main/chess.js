// Chess Game Logic

// Piece symbols
const PIECES = {
    white: {
        king: '♔',
        queen: '♕',
        rook: '♖',
        bishop: '♗',
        knight: '♘',
        pawn: '♙'
    },
    black: {
        king: '♚',
        queen: '♛',
        rook: '♜',
        bishop: '♝',
        knight: '♞',
        pawn: '♟'
    }
};

class ChessGame {
    constructor() {
        this.board = this.initializeBoard();
        this.currentPlayer = 'white';
        this.selectedSquare = null;
        this.validMoves = [];
        this.moveHistory = [];
        this.capturedPieces = { white: [], black: [] };
        this.isGameOver = false;

        this.renderBoard();
        this.attachEventListeners();
    }

    initializeBoard() {
        const board = Array(8).fill(null).map(() => Array(8).fill(null));

        // Place black pieces
        board[0] = [
            { type: 'rook', color: 'black' },
            { type: 'knight', color: 'black' },
            { type: 'bishop', color: 'black' },
            { type: 'queen', color: 'black' },
            { type: 'king', color: 'black' },
            { type: 'bishop', color: 'black' },
            { type: 'knight', color: 'black' },
            { type: 'rook', color: 'black' }
        ];
        board[1] = Array(8).fill({ type: 'pawn', color: 'black' });

        // Place white pieces
        board[6] = Array(8).fill({ type: 'pawn', color: 'white' });
        board[7] = [
            { type: 'rook', color: 'white' },
            { type: 'knight', color: 'white' },
            { type: 'bishop', color: 'white' },
            { type: 'queen', color: 'white' },
            { type: 'king', color: 'white' },
            { type: 'bishop', color: 'white' },
            { type: 'knight', color: 'white' },
            { type: 'rook', color: 'white' }
        ];

        return board;
    }

    renderBoard() {
        const boardElement = document.getElementById('chess-board');
        boardElement.innerHTML = '';

        for (let row = 0; row < 8; row++) {
            for (let col = 0; col < 8; col++) {
                const square = document.createElement('div');
                square.className = `square ${(row + col) % 2 === 0 ? 'light' : 'dark'}`;
                square.dataset.row = row;
                square.dataset.col = col;

                const piece = this.board[row][col];
                if (piece) {
                    const pieceElement = document.createElement('span');
                    pieceElement.className = 'piece';
                    pieceElement.textContent = PIECES[piece.color][piece.type];
                    square.appendChild(pieceElement);
                }

                boardElement.appendChild(square);
            }
        }

        this.updateStatus();
    }

    attachEventListeners() {
        const boardElement = document.getElementById('chess-board');
        boardElement.addEventListener('click', (e) => this.handleSquareClick(e));

        document.getElementById('new-game-btn').addEventListener('click', () => this.newGame());
        document.getElementById('undo-btn').addEventListener('click', () => this.undoMove());
    }

    handleSquareClick(e) {
        if (this.isGameOver) return;

        const square = e.target.closest('.square');
        if (!square) return;

        const row = parseInt(square.dataset.row);
        const col = parseInt(square.dataset.col);

        if (this.selectedSquare) {
            // Try to move the piece
            if (this.isValidMove(this.selectedSquare.row, this.selectedSquare.col, row, col)) {
                this.movePiece(this.selectedSquare.row, this.selectedSquare.col, row, col);
                this.clearSelection();
            } else if (this.board[row][col] && this.board[row][col].color === this.currentPlayer) {
                // Select a different piece
                this.selectSquare(row, col);
            } else {
                this.clearSelection();
            }
        } else {
            // Select a piece
            if (this.board[row][col] && this.board[row][col].color === this.currentPlayer) {
                this.selectSquare(row, col);
            }
        }
    }

    selectSquare(row, col) {
        this.clearSelection();
        this.selectedSquare = { row, col };
        this.validMoves = this.getValidMoves(row, col);

        // Highlight selected square
        const squares = document.querySelectorAll('.square');
        squares[row * 8 + col].classList.add('selected');

        // Highlight valid moves
        this.validMoves.forEach(move => {
            const square = squares[move.row * 8 + move.col];
            square.classList.add('valid-move');
            if (this.board[move.row][move.col]) {
                square.classList.add('can-capture');
            }
        });
    }

    clearSelection() {
        this.selectedSquare = null;
        this.validMoves = [];
        document.querySelectorAll('.square').forEach(square => {
            square.classList.remove('selected', 'valid-move', 'can-capture');
        });
    }

    movePiece(fromRow, fromCol, toRow, toCol) {
        const piece = this.board[fromRow][fromCol];
        const capturedPiece = this.board[toRow][toCol];

        // Capture piece if exists
        if (capturedPiece) {
            this.capturedPieces[capturedPiece.color].push(capturedPiece.type);
            this.updateCapturedPieces();
        }

        // Move the piece
        this.board[toRow][toCol] = piece;
        this.board[fromRow][fromCol] = null;

        // Record move
        const moveNotation = this.getMoveNotation(fromRow, fromCol, toRow, toCol, piece, capturedPiece);
        this.moveHistory.push({ fromRow, fromCol, toRow, toCol, piece, capturedPiece, notation: moveNotation });
        this.updateMoveHistory();

        // Switch player
        this.currentPlayer = this.currentPlayer === 'white' ? 'black' : 'white';

        // Re-render board
        this.renderBoard();

        // Check for game over
        this.checkGameOver();
    }

    getMoveNotation(fromRow, fromCol, toRow, toCol, piece, capturedPiece) {
        const cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'];
        const rows = ['8', '7', '6', '5', '4', '3', '2', '1'];

        let notation = '';
        if (piece.type !== 'pawn') {
            notation += piece.type[0].toUpperCase();
        }
        notation += cols[fromCol] + rows[fromRow];
        notation += capturedPiece ? 'x' : '-';
        notation += cols[toCol] + rows[toRow];

        return notation;
    }

    isValidMove(fromRow, fromCol, toRow, toCol) {
        return this.validMoves.some(move => move.row === toRow && move.col === toCol);
    }

    getValidMoves(row, col) {
        const piece = this.board[row][col];
        if (!piece) return [];

        let moves = [];

        switch (piece.type) {
            case 'pawn':
                moves = this.getPawnMoves(row, col, piece.color);
                break;
            case 'rook':
                moves = this.getRookMoves(row, col, piece.color);
                break;
            case 'knight':
                moves = this.getKnightMoves(row, col, piece.color);
                break;
            case 'bishop':
                moves = this.getBishopMoves(row, col, piece.color);
                break;
            case 'queen':
                moves = this.getQueenMoves(row, col, piece.color);
                break;
            case 'king':
                moves = this.getKingMoves(row, col, piece.color);
                break;
        }

        return moves;
    }

    getPawnMoves(row, col, color) {
        const moves = [];
        const direction = color === 'white' ? -1 : 1;
        const startRow = color === 'white' ? 6 : 1;

        // Forward move
        if (this.isInBounds(row + direction, col) && !this.board[row + direction][col]) {
            moves.push({ row: row + direction, col });

            // Double move from start
            if (row === startRow && !this.board[row + 2 * direction][col]) {
                moves.push({ row: row + 2 * direction, col });
            }
        }

        // Diagonal captures
        [-1, 1].forEach(colOffset => {
            const newRow = row + direction;
            const newCol = col + colOffset;
            if (this.isInBounds(newRow, newCol) &&
                this.board[newRow][newCol] &&
                this.board[newRow][newCol].color !== color) {
                moves.push({ row: newRow, col: newCol });
            }
        });

        return moves;
    }

    getRookMoves(row, col, color) {
        return this.getLinearMoves(row, col, color, [
            [-1, 0], [1, 0], [0, -1], [0, 1]
        ]);
    }

    getBishopMoves(row, col, color) {
        return this.getLinearMoves(row, col, color, [
            [-1, -1], [-1, 1], [1, -1], [1, 1]
        ]);
    }

    getQueenMoves(row, col, color) {
        return this.getLinearMoves(row, col, color, [
            [-1, 0], [1, 0], [0, -1], [0, 1],
            [-1, -1], [-1, 1], [1, -1], [1, 1]
        ]);
    }

    getLinearMoves(row, col, color, directions) {
        const moves = [];

        directions.forEach(([dRow, dCol]) => {
            let newRow = row + dRow;
            let newCol = col + dCol;

            while (this.isInBounds(newRow, newCol)) {
                if (!this.board[newRow][newCol]) {
                    moves.push({ row: newRow, col: newCol });
                } else {
                    if (this.board[newRow][newCol].color !== color) {
                        moves.push({ row: newRow, col: newCol });
                    }
                    break;
                }
                newRow += dRow;
                newCol += dCol;
            }
        });

        return moves;
    }

    getKnightMoves(row, col, color) {
        const moves = [];
        const offsets = [
            [-2, -1], [-2, 1], [-1, -2], [-1, 2],
            [1, -2], [1, 2], [2, -1], [2, 1]
        ];

        offsets.forEach(([dRow, dCol]) => {
            const newRow = row + dRow;
            const newCol = col + dCol;

            if (this.isInBounds(newRow, newCol) &&
                (!this.board[newRow][newCol] || this.board[newRow][newCol].color !== color)) {
                moves.push({ row: newRow, col: newCol });
            }
        });

        return moves;
    }

    getKingMoves(row, col, color) {
        const moves = [];
        const offsets = [
            [-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 1],
            [1, -1], [1, 0], [1, 1]
        ];

        offsets.forEach(([dRow, dCol]) => {
            const newRow = row + dRow;
            const newCol = col + dCol;

            if (this.isInBounds(newRow, newCol) &&
                (!this.board[newRow][newCol] || this.board[newRow][newCol].color !== color)) {
                moves.push({ row: newRow, col: newCol });
            }
        });

        return moves;
    }

    isInBounds(row, col) {
        return row >= 0 && row < 8 && col >= 0 && col < 8;
    }

    updateStatus() {
        const playerDisplay = document.getElementById('current-player');
        const statusMessage = document.getElementById('status-message');

        if (this.isGameOver) {
            playerDisplay.textContent = 'Game Over!';
            statusMessage.textContent = `${this.currentPlayer === 'white' ? 'Black' : 'White'} wins!`;
        } else {
            playerDisplay.textContent = `${this.currentPlayer === 'white' ? 'White' : 'Black'}'s Turn`;
            statusMessage.textContent = 'Select a piece to move';
        }
    }

    updateMoveHistory() {
        const moveList = document.getElementById('move-list');
        const lastMove = this.moveHistory[this.moveHistory.length - 1];

        if (lastMove) {
            const moveItem = document.createElement('div');
            moveItem.className = 'move-item';
            moveItem.textContent = `${this.moveHistory.length}. ${lastMove.notation}`;
            moveList.appendChild(moveItem);
            moveList.scrollTop = moveList.scrollHeight;
        }
    }

    updateCapturedPieces() {
        ['white', 'black'].forEach(color => {
            const container = document.getElementById(`captured-${color}`);
            container.innerHTML = '';

            this.capturedPieces[color].forEach(pieceType => {
                const pieceElement = document.createElement('span');
                pieceElement.className = 'captured-piece';
                pieceElement.textContent = PIECES[color][pieceType];
                container.appendChild(pieceElement);
            });
        });
    }

    checkGameOver() {
        // Simple game over check - if king is captured
        let whiteKing = false;
        let blackKing = false;

        for (let row = 0; row < 8; row++) {
            for (let col = 0; col < 8; col++) {
                const piece = this.board[row][col];
                if (piece && piece.type === 'king') {
                    if (piece.color === 'white') whiteKing = true;
                    if (piece.color === 'black') blackKing = true;
                }
            }
        }

        if (!whiteKing || !blackKing) {
            this.isGameOver = true;
            this.updateStatus();
        }
    }

    undoMove() {
        if (this.moveHistory.length === 0) return;

        const lastMove = this.moveHistory.pop();

        // Restore piece positions
        this.board[lastMove.fromRow][lastMove.fromCol] = lastMove.piece;
        this.board[lastMove.toRow][lastMove.toCol] = lastMove.capturedPiece;

        // Restore captured pieces
        if (lastMove.capturedPiece) {
            const color = lastMove.capturedPiece.color;
            const index = this.capturedPieces[color].lastIndexOf(lastMove.capturedPiece.type);
            if (index > -1) {
                this.capturedPieces[color].splice(index, 1);
            }
        }

        // Switch player back
        this.currentPlayer = this.currentPlayer === 'white' ? 'black' : 'white';

        // Update display
        this.renderBoard();
        this.updateCapturedPieces();

        // Update move history display
        const moveList = document.getElementById('move-list');
        if (moveList.lastChild) {
            moveList.removeChild(moveList.lastChild);
        }

        this.isGameOver = false;
    }

    newGame() {
        this.board = this.initializeBoard();
        this.currentPlayer = 'white';
        this.selectedSquare = null;
        this.validMoves = [];
        this.moveHistory = [];
        this.capturedPieces = { white: [], black: [] };
        this.isGameOver = false;

        document.getElementById('move-list').innerHTML = '';
        this.renderBoard();
        this.updateCapturedPieces();
    }
}

// Initialize game when page loads
document.addEventListener('DOMContentLoaded', () => {
    new ChessGame();
});
