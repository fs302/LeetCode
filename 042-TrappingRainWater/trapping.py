import json
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_wall = []      # figure out highest wall of the position's left
        right_wall = []     # figure out highest wall of the position's right
        n = len(height)
        cur_left = 0
        cur_right = 0
        for p in range(n):
            left_wall.append(cur_left)
            right_wall.insert(0,cur_right)
            if height[p] > cur_left:
                cur_left = height[p]
            if height[n-p-1] > cur_right:
                cur_right = height[n-p-1]
        amount = 0
        for p in range(n):
            if height[p] < min(left_wall[p],right_wall[p]):
                amount += min(left_wall[p],right_wall[p]) - height[p]
        return amount
        

def stringToIntegerList(input):
    return json.loads(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            height = stringToIntegerList(line)
            
            ret = Solution().trap(height)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()