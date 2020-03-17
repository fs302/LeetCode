import json
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        i = 0
        while i < l:
            num = nums[i]
            if num == i+1:
                i += 1
            elif num < 1 or num > l or num == nums[num-1]: #case1&2: out of range, case3: got this num on right place, so nums[i] can be replaced
                nums[i] = nums[l-1] # Get new candidate from the end
                l -= 1
            else:
                nums[i] = nums[num-1] 
                nums[num-1] = num   # swap with the right place number
        return l+1


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
            
            ret = Solution().firstMissingPositive(nums)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()