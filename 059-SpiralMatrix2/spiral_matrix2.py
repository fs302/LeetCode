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
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0]*n for i in range(n)] # False Example: matrix = [[0]*n] * n (shallow copy)
        pi, pj = 0, 0
        dirs = ['right','down','left','up']
        dir_index = 0
        matrix[pi][pj] = 1
        counter = 1
        while counter < n*n:
            ni, nj = self.getNext(pi, pj, dirs[dir_index])
            while ni<0 or ni>=n or nj<0 or nj>=n or matrix[ni][nj] != 0:
                dir_index = (dir_index + 1) % 4
                ni, nj = self.getNext(pi, pj, dirs[dir_index])
            pi, pj = ni, nj
            if 0<=pi<n and 0<=pj<n and matrix[pi][pj] == 0:
                matrix[pi][pj] = counter+1
            counter += 1

        return matrix


def stringToInt(input):
    return int(input)

def int2dArrayToString(input):
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
            
            ret = Solution().generateMatrix(n)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()