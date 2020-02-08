import sys
import json

class Solution(object):
    
    def swap(self, nums, i, j):
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t
        return None
    
    def reverse(self, nums, start):
        i = start
        j = len(nums)-1
        while i < j:
            self.swap(nums, i, j)
            i += 1
            j -= 1
        return None
    
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        if nums is None or len(nums)<=1:
            return None
        n = len(nums)
        # from right to left, find first digit which is lower than its right, named A
        i = n-2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        # from right to left, choose the first digit which is larger than A, named B
        if i >= 0:
            j = n-1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            # swap A,B to get a larger number, but not the nearest
            self.swap(nums, i, j)
        # make it nearest larger number
        self.reverse(nums, i+1)
        return None

def stringToIntegerList(input):
    return json.loads(input)

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
            
            ret = Solution().nextPermutation(nums)

            out = integerListToString(nums)
            if ret is not None:
                print "Do not return anything, modify nums in-place instead."
            else:
                print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()