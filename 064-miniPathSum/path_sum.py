class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid is None or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        f = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    better = 0
                elif i == 0:
                    better = f[i][j-1]
                elif j == 0:
                    better = f[i-1][j]
                else:
                    better = min(f[i-1][j],f[i][j-1])
                f[i][j] = better + grid[i][j]
        return f[m-1][n-1]

def main():
    grid = [[1,2,3],[4,5,6]]
    ret = Solution().minPathSum(grid)
    print(ret)

if __name__ == '__main__':
    main()