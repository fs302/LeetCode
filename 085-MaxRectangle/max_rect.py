import json
from typing import List 

class Solution:
    def currentMaxArea(self, vector: List[int]) -> int:
        max_space = 0 
        heights = vector.copy()
        # Sentinel
        heights.insert(0,0)
        heights.append(0)
        stack = [0] # current highest bar's position
        for i in range(1,len(heights)):
            h = heights[i]
            while len(stack) > 0 and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                left = stack[-1] + 1
                right = i - 1
                width = right - left + 1
                s = height * width
                max_space = max(max_space, s)
            stack.append(i)
            
        return max_space

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0
        if matrix is None or len(matrix) == 0:
            return 0
        current_heights = [0] * len(matrix[0])
        for line in matrix:
            for i,st in enumerate(line):
                current_heights[i] = current_heights[i] + 1 if st=='1' else 0
            print(current_heights)
            ans = max(ans, self.currentMaxArea(current_heights))
        return ans

def main():
    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    ret = Solution().maximalRectangle(matrix)
    print(ret)


if __name__ == '__main__':
    main()