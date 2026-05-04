from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        sq = defaultdict(set)

        for i in range(9):
            for j in range(9):
                # Pass when empty
                if board[i][j] == '.':
                    continue

                # Row check
                if board[i][j] in row[i]:
                    return False
                row[i].add(board[i][j])

                # Column check
                if board[i][j] in col[j]:
                    return False
                col[j].add(board[i][j])

                # Square check
                key = (i // 3, j // 3) # Hashable tuple to serve as 3 x 3 matrix key)
                if board[i][j] in sq[key]:
                    return False
                sq[key].add(board[i][j])

        return True