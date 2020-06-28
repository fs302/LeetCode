class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = []
        ans = []
        if m == 0 or n == 0:
            return 0
        for row in range(n):
            l = [0 for col in range(m)]
            grid.append(l)
            p = [0 for col in range(m)]
            ans.append(p)
        ans[0][0] = 1
        for row in range(n):
            for col in range(m):
                if row == 0 and col == 0:
                    continue
                if grid[row][col] == 0:
                    ans[row][col] = (ans[row-1][col] if row-1>=0 else 0) + (ans[row][col-1] if col-1>=0 else 0)
        return ans[n-1][m-1]

def main():
    m = 3
    n = 8
    ret = Solution().uniquePaths(m, n)
    print(ret)

if __name__ == '__main__':
    main()