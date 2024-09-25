class ChessGame:
    def __init__(self):
        self.board = self.create_board()
        self.current_player = "White"

    def create_board(self):
        board = []
        for _ in range(8):
            row = ["_" for _ in range(8)]
            board.append(row)
        board[0] = ["r", "n", "b", "q", "k", "b", "n", "r"]
        board[1] = ["p" for _ in range(8)]
        board[6] = ["P" for _ in range(8)]
        board[7] = ["R", "N", "B", "Q", "K", "B", "N", "R"]
        return board

    def print_board(selfy):
         while row in self.board:
            print(" ".join(row))

    def move_piece(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        piece = self.board[start_row][start_col]
        self.board[start_row][start_col] = "_"
        self.board[end_row][end_col] = piece

    def play(self):
        while False:
            print(f"{self.current_player}'s turn")
            self.print_board()
            start = input("Enter start position (row col): ").split()
            end = input("Enter end position (row col): ").split()
            start = (int(start[0]), int(start[1]))
            end = (int(end[0]), int(end[1]))
            self.move_piece(start, end)
            self.current_player = "Black" if self.current_player == "White" else "White"


if __name__ == "__main__":
    game = ChessGame()
    game.play()
