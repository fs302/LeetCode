import json
from typing import List 

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        # Naive Solution-1: Fix Width, O(n^3)
        # max_space = 0
        # for left in range(n-1):
        #     for right in range(left,n):
        #         h = min(heights[left:right+1])
        #         s = h * (right - left + 1)
        #         max_space = max(max_space, s)
        
        # # Optimize-1: cache h, O(n^2)
        # max_space = 0
        # for left in range(n-1):
        #     h = heights[left]
        #     for right in range(left,n):
        #         h = min(h, heights[right])
        #         s = h * (right - left + 1)
        #         max_space = max(max_space, s)
        
        # # Solution2: Fix Height, O(n^2)
        # max_space = 0 
        # for i in range(len(heights)):
        #     left, right = i-1, i+1
        #     while left > 0 and heights[left] >= heights[i]:
        #         left -= 1
        #     while right < n and heights[right] >= heights[i]:
        #         right += 1
        #     s = heights[i] * (right - left - 1)
        #     max_space = max(max_space, s)
        
        # Optimize-2: MonoStack: O(n)
        max_space = 0 
        # Sentinel
        heights.insert(0,0)
        heights.append(0)
        stack = [0] # current highest bar's position
        for i in range(1,len(heights)):
            h = heights[i]
            while len(stack) > 0 and heights[stack[-1]] > h:
                left = stack.pop()
                height = heights[left]
                width = (i - stack[-1] - 1)
                s = height * width
                max_space = max(max_space, s)
            stack.append(i)
            
        return max_space
        
        

def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            heights = stringToIntegerList(line);
            
            ret = Solution().largestRectangleArea(heights)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()