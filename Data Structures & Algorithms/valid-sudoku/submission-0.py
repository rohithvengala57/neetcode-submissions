from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Checking rows and columns
        for i in range(9):
            checkCol = [0] * 9
            checkRow = [0] * 9
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j]) - 1  
                    if checkRow[num] == 1:
                        return False
                    checkRow[num] = 1
                
                if board[j][i] != ".":
                    num = int(board[j][i]) - 1
                    if checkCol[num] == 1:
                        return False
                    checkCol[num] = 1

        # Checking 3x3 sub-boxes
        check = [[[0 for _ in range(9)] for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    num = int(board[i][j]) - 1
                    box_row, box_col = i // 3, j // 3
                    if check[box_row][box_col][num] == 1:
                        return False
                    check[box_row][box_col][num] = 1

        return True
