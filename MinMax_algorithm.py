class MinMax:
    def __init__(self, board):
        self.GameBoard = board

    def evaluate(self):
        # Rows
        for row in range(3):
            if self.GameBoard[row][0] == self.GameBoard[row][1] == self.GameBoard[row][2] != '-':
                return 1 if self.GameBoard[row][0] == 'x' else -1
        # Columns
        for col in range(3):
            if self.GameBoard[0][col] == self.GameBoard[1][col] == self.GameBoard[2][col] != '-':
                return 1 if self.GameBoard[0][col] == 'x' else -1
        # Diagonals
        if self.GameBoard[0][0] == self.GameBoard[1][1] == self.GameBoard[2][2] != '-':
            return 1 if self.GameBoard[1][1] == 'x' else -1
        if self.GameBoard[0][2] == self.GameBoard[1][1] == self.GameBoard[2][0] != '-':
            return 1 if self.GameBoard[1][1] == 'x' else -1
        # Still moves left?
        for row in self.GameBoard:
            if '-' in row:
                return 2
        return 0

    def max(self):
        score = self.evaluate()
        if score != 2:
            return (score, 0, 0)

        best_score, best_move = -2, (0, 0)
        for r in range(3):
            for c in range(3):
                if self.GameBoard[r][c] == '-':
                    self.GameBoard[r][c] = 'x'
                    current_score = self.min()[0]
                    self.GameBoard[r][c] = '-'
                    if current_score > best_score:
                        best_score, best_move = current_score, (r, c)
        return (best_score, best_move[0], best_move[1])

    def min(self):
        score = self.evaluate()
        if score != 2:
            return (score, 0, 0)

        best_score, best_move = 2, (0, 0)
        for r in range(3):
            for c in range(3):
                if self.GameBoard[r][c] == '-':
                    self.GameBoard[r][c] = 'o'
                    current_score = self.max()[0]
                    self.GameBoard[r][c] = '-'
                    if current_score < best_score:
                        best_score, best_move = current_score, (r, c)
        return (best_score, best_move[0], best_move[1])
