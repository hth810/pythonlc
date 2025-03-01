class Solution:
    def __init__(self):
        self.res = []

    def isValid(self, board, row, col):
        n=len(board)
        for i in range(0,row+1):
            if board[i][col]=='Q':
                return False
        for i,j in zip(range(row-1,-1,-1),range(col+1,n)):
            if board[i][j]=='Q':
                return False
        for i,j in zip(range(row-1,-1,-1),range(col-1,-1,-1)):
            if board[i][j]=='Q':
                return False
        return True
    def backtrack(self, board, row):
        if row==len(board):
            self.res.append(board.copy())
            return
        for col in range(len(board)):
            # 排除不合法选择
            if not self.isValid(board, row, col):
                continue
            # 做选择
            board[row]=board[row][:col]+'Q'+board[row][col+1:]
            # 进入下一行决策
            self.backtrack(board, row+1)
            # 撤销选择
            board[row]=board[row][:col]+'.'+board[row][col+1:]
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ['.' * n for _ in range(n)]
        self.backtrack(board, 0)
        return self.res