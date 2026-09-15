class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        out = False
        count = 0
        sub_box = []
        for i in range(0,9):
            column = []
            row = []
            for j in range(0,9):
                if board[i][j] in row and board[i][j] != '.':
                    return out
                else:
                    row.append(board[i][j])

                if board[j][i] in column and board[j][i] != '.':
                    return out
                else: 
                    column.append(board[j][i])
                
                if i%3 == 0 and j%3 == 0:
                    sub_box = []
                    for k in range(i,i+3):
                        for l in range(j,j+3):
                            if board[k][l] in sub_box and board[k][l] != '.':
                                return out
                            else:
                                sub_box.append(board[k][l])

        return True
    