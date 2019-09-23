import json

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        i = 0
        for j in range(1,len(nums)):
            if (nums[j] != nums[i]):
                i += 1
                nums[i] = nums[j]
        return i+1

def stringToIntegerList(input):
    return json.loads(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

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
            
            ret = Solution().removeDuplicates(nums)

            out = integerListToString(nums, len_of_list=ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()