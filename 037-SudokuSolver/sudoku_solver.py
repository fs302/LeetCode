import json

class Solution(object):
    def __init__(self):
        self.result_board = None
        self.dim = 9
        self.flag = False
        self.count = 0
        
    def check(self, board, row, col):
        """
        check if input [row][col] make a valid sudoku
        """
        row_list = []
        col_list = []
        block_list = []
        for j in range(self.dim):
            if board[row][j] != '.':
                if board[row][j] not in row_list:
                    row_list.append(board[row][j])
                else:
                    return False
        for i in range(self.dim):
            if board[i][col] != '.':
                if board[i][col] not in col_list:
                    col_list.append(board[i][col])
                else:
                    return False
        row_start = row/3*3
        col_start = col/3*3
        for i in range(row_start,row_start+3):
            for j in range(col_start,col_start+3):
                if i/3 == row/3 and j/3 == col/3:
                    if board[i][j] != '.':
                        if board[i][j] not in block_list:
                            block_list.append(board[i][j])
                        else:
                            return False
        return True
                
    def dfs(self, board, depth):
        """
        depth first search for a valid solution
        """
        if depth > 80:
            self.result_board = board
            return True
        row = depth / self.dim
        col = depth % self.dim
        # print(depth, row, col, board[row][col])
        if board[row][col] != '.':
            return self.dfs(board,depth+1)
        for num in range(1,self.dim+1):
            tmp = board[row][col]
            board[row][col] = str(num)
            if self.check(board, row, col):
                res = self.dfs(board,depth+1)
                if res:
                    return True
            board[row][col] = tmp
        
        return False
    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if self.dfs(board,0):
            board = self.result_board
        return None

def stringToChar2dArray(input):
    return json.loads(input)

def char2dArrayToString(input):
    return json.dumps(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            board = stringToChar2dArray(line)
            
            ret = Solution().solveSudoku(board)

            out = char2dArrayToString(board)
            if ret is not None:
                print "Do not return anything, modify board in-place instead."
            else:
                print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()