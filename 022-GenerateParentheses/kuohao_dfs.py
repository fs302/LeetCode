import json

class Solution(object):
    
    def __init__(self):
        self.candidates = []
        
    def dfs(self, end_num, status, pool):
        if end_num == 1 and pool == 0:
            res = status + ')'
            self.candidates.append(res)
            return
        if pool > 0:
            self.dfs(end_num+1, status+'(', pool-1)
        if end_num > 0:
            self.dfs(end_num-1, status+')', pool)
        return
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.dfs(0,"",n)
        return self.candidates

def stringToInt(input):
    return int(input)

def stringArrayToString(input):
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
            
            ret = Solution().generateParenthesis(n)

            out = stringArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()