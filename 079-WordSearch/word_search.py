import time
class Solution(object):
    def __init__(self):
        self.board = []
        self.word = ""
    
    def dfs(self, status, now_i, now_j, st):
        if len(st) == len(self.word):
            return True
        neighbors = [(now_i-1,now_j),(now_i,now_j-1),(now_i,now_j+1),(now_i+1,now_j)]
        ret = False
        for i,j in neighbors:
            # print(now_i, now_j, i, j)
            if i >= 0 and i < len(status) and j >= 0 and j < len(status[0]) and status[i][j] == 0:
                ch = self.board[i][j]
                if ch == self.word[len(st)] and not ret:
                    st = st + ch
                    status[i][j] = 1
                    ret = ret | self.dfs(status, i, j, st)
                    st = st[:-1]
                    status[i][j] = 0
        return ret

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        status = [[0 for j in range(len(board[0]))] for i in range(len(board))]
        
        self.board = board
        self.word = word

        st = ''
        ret = False
        for i in range(len(board)):
            for j in range(len(board[i])):
                ch = board[i][j]
                if ch == word[len(st)] and not ret:
                    st += ch
                    status[i][j] = 1 
                    ret = ret | self.dfs(status, i, j, st)
                    status[i][j] = 0 
                    st = st[:-1]
        return ret 

def main():
    s = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    print(s.exist(board, word))


if __name__ == '__main__':
    main()     