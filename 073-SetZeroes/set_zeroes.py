class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # Naive Solution
        
        row = [1 for i in range(len(matrix))]
        col = [1 for i in range(len(matrix[0]))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if row[i] == 0 or col[j] == 0:
                    matrix[i][j] = 0
        
        return matrix

def main():
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    ret = Solution().setZeroes(matrix)
    print(ret)

if __name__ == '__main__':
    main()     