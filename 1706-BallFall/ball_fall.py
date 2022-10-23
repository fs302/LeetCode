class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        # pre-process
        action_matrix = []
        m, n = len(grid), len(grid[0])
        for row in range(m):
            row_action = []
            for col in range(n):
                # default: stuck at 'V'
                action = -1
                # condition-1: move-right
                if grid[row][col] == 1 \
                    and col+1 < n \
                    and grid[row][col+1] == 1:
                        action = col + 1
                # condition-2: move-left
                if grid[row][col] == -1 \
                    and col-1 >= 0 \
                    and grid[row][col-1] == -1:
                        action = col - 1
                row_action.append(action)
            action_matrix.append(row_action)

        # run-process
        results = []
        for col in range(n):
            ans = -1
            row = 0 
            while row < m:
                if action_matrix[row][col] != -1:
                    col = action_matrix[row][col]
                    row += 1
                else:
                    break
            if row == m:
                ans = col
            results.append(ans)

        return results