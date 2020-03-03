import json

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # handle outliers
        if len(nums) == 0 or target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        # binary search
        left, right = 0, len(nums) - 1
        mid = (left + right) / 2 
        while nums[mid] != target and left + 1 < right:
            if nums[mid] > target:
                right = mid
            else:
                left = mid 
            mid = (left + right) / 2
        if nums[mid] == target:
            return mid
        return mid+1

def stringToIntegerList(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

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
            line = lines.next()
            target = stringToInt(line)
            
            ret = Solution().searchInsert(nums, target)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()