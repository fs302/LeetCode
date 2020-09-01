class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        i, j = 0,0
        # macro-search
        while i < m-1 and matrix[i+1][0] <= target:
            i += 1
        # micro-search
        while j < n-1 and matrix[i][j] < target:
            j += 1
        if matrix[i][j] == target:  
            return True
        return False
            
def main():
    matrix = [[1],[3]]
    target = 3
    ret = Solution().searchMatrix(matrix, target)
    print(ret)

    matrix = []
    target = 3
    ret = Solution().searchMatrix(matrix, target)
    print(ret)

    matrix = [[]]
    target = 3
    ret = Solution().searchMatrix(matrix, target)
    print(ret)

    matrix = [[3],[33]]
    target = 3
    ret = Solution().searchMatrix(matrix, target)
    print(ret)

if __name__ == '__main__':
    main()     