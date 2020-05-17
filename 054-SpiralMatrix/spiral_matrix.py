import json
class Solution(object):
    def getNext(self, x, y, direction):
        if direction == 'right':
            return x,y+1
        if direction == 'down':
            return x+1,y
        if direction == 'left':
            return x, y-1
        if direction == 'up':
            return x-1, y
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if matrix == None or len(matrix) == 0:
            return res
        m = len(matrix)
        n = len(matrix[0])
        x, y = 0, 0
        dirs = ['right','down','left','up']
        dir_i = 0
        res.append(matrix[x][y])
        matrix[x][y] = None
        count = 1
        while count < n*m:
            nx, ny = self.getNext(x,y,dirs[dir_i])
            # trial-adjust
            while nx < 0 or nx >= m or ny < 0 or ny >= n or matrix[nx][ny] == None:
                dir_i = (dir_i+1) % 4
                nx, ny = self.getNext(x,y,dirs[dir_i])
            if matrix[nx][ny] != None:
                x, y = nx, ny
                res.append(matrix[x][y])
                matrix[x][y] = None
                count += 1
        return res

def stringToInt2dArray(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            matrix = stringToInt2dArray(line)
            
            ret = Solution().spiralOrder(matrix)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()