import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt

# Chessboard dimensions
ROWS = 8
COLS = 8

# Piece colors
WHITE = "white"
BLACK = "black"

# Piece types
PAWN = "pawn"
ROOK = "rook"
KNIGHT = "knight"
BISHOP = "bishop"
QUEEN = "queen"
KING = "king"

# Unicode characters for chess pieces
PIECE_UNICODE = {
    (WHITE, PAWN): "♙",
    (WHITE, ROOK): "♖",
    (WHITE, KNIGHT): "♘",
    (WHITE, BISHOP): "♗",
    (WHITE, QUEEN): "♕",
    (WHITE, KING): "♔",
    (BLACK, PAWN): "♟",
    (BLACK, ROOK): "♜",
    (BLACK, KNIGHT): "♞",
    (BLACK, BISHOP): "♝",
    (BLACK, QUEEN): "♛",
    (BLACK, KING): "♚"
}


class ChessPiece:
    def __init__(self, color, piece_type):
        self.color = color
        self.piece_type = piece_type

    def get_unicode(self):
        return PIECE_UNICODE[(self.color, self.piece_type)]


class Chessboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.grid = QGridLayout()
        self.grid.setSpacing(0)

        self.pieces = [[None for _ in range(COLS)] for _ in range(ROWS)]

        self.create_pieces()

        self.setLayout(self.grid)

    def create_pieces(self):
        for row in range(ROWS):
            for col in range(COLS):
                piece = None
                if row == 1:
                    piece = ChessPiece(BLACK, PAWN)
                elif row == 6:
                    piece = ChessPiece(WHITE, PAWN)
                elif row == 0 or row == 7:
                    if col == 0 or col == 7:
                        piece = ChessPiece(BLACK, ROOK)
                    elif col == 1 or col == 6:
                        piece = ChessPiece(BLACK, KNIGHT)
                    elif col == 2 or col == 5:
                        piece = ChessPiece(BLACK, BISHOP)
                    elif col == 3:
                        piece = ChessPiece(BLACK, QUEEN)
                    elif col == 4:
                        piece = ChessPiece(BLACK, KING)
                if piece:
                    self.add_piece(piece, row, col)

    def add_piece(self, piece, row, col):
        button = QPushButton(self)
        button.setFont(QFont("Arial", 32, QFont.Bold))
        button.setText(piece.get_unicode())
        button.setFixedSize(80, 80)
        button.setObjectName(f"button_{row}_{col}")
        button.clicked.connect(self.piece_clicked)

        self.pieces[row][col] = piece

        self.grid.addWidget(button, row, col)

    def piece_clicked(self):
        button = self.sender()
        row, col = map(int, button.objectName().split("_")[1:])
        piece = self.pieces[row][col]
        if piece:
            print(f"Clicked piece: {piece.color} {piece.piece_type} at ({row}, {col})")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Chess Game")
        self.setWindowIcon(QIcon("images/chess_icon.png"))

        self.chessboard = Chessboard()
        self.setCentralWidget(self.chessboard)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
