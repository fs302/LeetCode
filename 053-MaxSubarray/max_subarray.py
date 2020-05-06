import json
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dynamic-programming version
        if len(nums) == 0:
            return 0
        
        opt = [None,nums[0]] 
        # [0] stands for exclude-this-item, [1] stands for include-this-item

        def ext_max(arg1, arg2):
            if arg1 is None:
                return arg2
            return max(arg1, arg2)
        
        for num in nums[1:]:
            opt[0] = ext_max(opt[0],opt[1])
            opt[1] = ext_max(num, opt[1] + num)
      
        return ext_max(opt[0],opt[1])

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
            nums = stringToIntegerList(line)
            
            ret = Solution().maxSubArray(nums)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()