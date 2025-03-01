class Solution:
    def __init__(self):
        self.res=0

    def isValid(self,board,row,col):
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

    def backtrack(self,board,row):
        if row==len(board):
            self.res+=1
            return
        for col in range(len(board)):
            if not self.isValid(board,row,col):
                continue
            board[row]=board[row][:col]+'Q'+board[row][col+1:]
            self.backtrack(board,row+1)
            board[row]=board[row][:col]+'.'+board[row][col+1:]

    def totalNQueens(self, n: int) -> int:
        board=['.'*n for _ in range(n)]
        self.backtrack(board,0)
        return self.res