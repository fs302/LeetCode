import json
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(int(n/2)):
            for j in range(i,n-i-1):
                t = matrix[i][j]
                c = n-1
                matrix[i][j] = matrix[c-j][i]
                matrix[c-j][i] = matrix[c-i][c-j]
                matrix[c-i][c-j] = matrix[j][c-i]
                matrix[j][c-i] = t

def stringToInt2dArray(input):
    return json.loads(input)

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
            matrix = stringToInt2dArray(line)
            
            ret = Solution().rotate(matrix)

            out = int2dArrayToString(matrix)
            if ret is not None:
                print "Do not return anything, modify matrix in-place instead."
            else:
                print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()