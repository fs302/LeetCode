class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        grid = obstacleGrid
        n = len(grid)
        m = len(grid[0])
        ans = []
        for row in range(n):
            p = [0 for col in range(m)]
            ans.append(p)
        if grid[0][0] == 0: # trap
            ans[0][0] = 1  
        for row in range(n):
            for col in range(m):
                if row == 0 and col == 0:
                    continue
                if grid[row][col] == 0:
                    ans[row][col] = (ans[row-1][col] if row-1>=0 else 0) + (ans[row][col-1] if col-1>=0 else 0)
        return ans[n-1][m-1]
        
def main():
    grid = [[1]]
    ret = Solution().uniquePathsWithObstacles(grid)
    print(ret)

if __name__ == '__main__':
    main()