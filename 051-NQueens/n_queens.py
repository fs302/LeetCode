import json
class Solution(object):
    def __init__(self):
        self.solution = []
        self.EXISTS = 1
        self.FREE = 0
        
    def check_flag(self, depth, pos, flag):
        if depth in flag['row'] and flag['row'][depth] == self.EXISTS:
            return False
        if pos in flag['col'] and flag['col'][pos] == self.EXISTS:
            return False
        if pos-depth in flag['leftx'] and flag['leftx'][pos-depth] == self.EXISTS:
            return False
        if pos+depth in flag['rightx'] and flag['rightx'][pos+depth] == self.EXISTS:
            return False
        return True
        
    def change_flag(self, depth, pos, flag, value):
        flag['row'][depth] = value
        flag['col'][pos] = value
        flag['leftx'][pos-depth] = value
        flag['rightx'][pos+depth] = value
        return None
        
    def formulation(self, state, n):
        result = []
        for pos in state:
            line = ''
            for i in range(n):
                if i == pos:
                    line += 'Q'
                else:
                    line += '.'
            result.append(line)
        return result

    def dfs(self, depth, state, flag, n):
        if depth == n:
            self.solution.append(self.formulation(state, n))
            return None
        
        for pos in range(n):
            # print(depth, pos, state, self.check_flag(depth, pos, flag))
            if self.check_flag(depth, pos, flag):
                state.append(pos)
                self.change_flag(depth, pos, flag, self.EXISTS)
                self.dfs(depth+1, state, flag, n)
                self.change_flag(depth, pos, flag, self.FREE)
                state.pop()
        return None
        
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        state = []
        self.solution = []
        flag = {'row':{}, 'col':{}, 'leftx':{}, 'rightx': {}}
        self.dfs(0, state, flag, n)
        return self.solution
        

def stringToInt(input):
    return int(input)

def string2dArrayToString(input):
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
            n = stringToInt(line)
            
            ret = Solution().solveNQueens(n)

            out = string2dArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()