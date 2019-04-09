class point(object):
    def __init__(self, numRows):
        self.x = 0 # row
        self.y = 0 # column
        self.numRows = numRows
        self.direction = 1
        
    def get_pos(self):
        return self.x, self.y
    
    def next(self):
        if self.x == self.numRows - 1:
            self.direction = -1
        if self.x == 0:
            self.direction = 1
        if self.numRows == 1:
            self.direction = 0
        if self.direction == 1: # go down
            self.x += 1
        else:
            self.x += self.direction # go ahead
            self.y += 1
        return self.x, self.y

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        p = point(numRows)
        result_line = [[] for i in range(numRows)]
        
        for i in range(len(s)):
            x,y = p.get_pos()
            # print s[i],x,y
            result_line[x].append(s[i])
            p.next()

        res = ''.join([''.join(line) for line in result_line])
        return res

def main():
    s = "PAYPALISHIRING"
    n = 3 
    solution = Solution()
    print s,n,solution.convert(s,n)

if __name__ == '__main__':
    main()