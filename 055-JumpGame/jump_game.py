import json
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cur_max = 0
        for i,jump in enumerate(nums):
            # print i, jump, cur_max
            if i > cur_max:
                return False
            if i+jump > cur_max:
                cur_max = i+jump
        if cur_max >= len(nums)-1:
            return True
        return False
            

def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            nums = stringToIntegerList(line)
            
            ret = Solution().canJump(nums)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()