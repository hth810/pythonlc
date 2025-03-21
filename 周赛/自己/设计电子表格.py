class Spreadsheet:

    def __init__(self, rows: int):
        self.table=[[0]*26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        i,j=self._parse_cell(cell)
        self.table[i][j]=value

    def resetCell(self, cell: str) -> None:
        i,j=self._parse_cell(cell)
        self.table[i][j]=0

    def _parse_cell(self, cell: str):
        ch = cell[0]
        row_str = cell[1:]
        row = int(row_str) - 1
        col = ord(ch) - ord('A')
        return (row, col)


    def getValue(self, formula: str) -> int:
        a=formula[1:]
        x,y=a.split('+')
        if self.judge(x):
            row_x,col_x=self._parse_cell(x)
            x_val=self.table[row_x][col_x]
        else:
            x_val=int(x)
        if self.judge(y):
            row_y,col_y=self._parse_cell(y)
            y_val=self.table[row_y][col_y]
        else:
            y_val=int(y)
        return x_val+y_val

    def judge(self,x):
        if 'A'<=x[0]<='Z':
            return True

        return False




# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)