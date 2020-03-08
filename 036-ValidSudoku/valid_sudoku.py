import json
class Solution(object):
    
    def __init__(self):
        self.flag_dict = {}
    
    def check_flag(self, space_name, num):
        """
        Atomic assertion check for the sudoku rule
        - space_name: may be row,column and square
        - num: the input number
        """
        # print("check space:%s, num:%s" % (space_name, num))
        if space_name not in self.flag_dict:
            self.flag_dict[space_name] = []
        if num in self.flag_dict[space_name]:
            return False
        self.flag_dict[space_name].append(num)
        return True
    
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    rule1 = self.check_flag('r'+str(i),board[i][j])
                    rule2 = self.check_flag('c'+str(j),board[i][j])
                    rule3 = self.check_flag(str(i/3)+str(j/3),board[i][j])
                    if not(rule1 and rule2 and rule3):
                        return False
        return True

def stringToChar2dArray(input):
    return json.loads(input)

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
            
            ret = Solution().isValidSudoku(board)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()