import json

class Solution(object):
    def binary_find(self, arr, target):
        if len(arr) <= 1:
            if len(arr) == 1 and arr[0] == target:
                return 0
            else:
                return -1
        mid_pos = len(arr)/2
        if arr[mid_pos] == target:
            return mid_pos
        left = self.binary_find(arr[:mid_pos],target)
        if left != -1:
            return left
        right = self.binary_find(arr[mid_pos+1:],target)
        if right != -1:
            return mid_pos+1+right
        return -1
    
    def find_first(self, nums, target, left, right):
        if left == right:
            return left
        if left+1 == right:
            return left if nums[left]==target else right
        mid = (left+right)/2
        if nums[mid] == target:
            return self.find_first(nums,target,left,mid)
        else:
            return self.find_first(nums,target,mid+1,right)
    
    def find_last(self, nums, target, left, right):
        if left == right:
            return right
        if left+1 == right:
            return right if nums[right]==target else left
        mid = (left+right)/2
        if nums[mid] == target:
            return self.find_last(nums,target,mid,right)
        else:
            return self.find_last(nums,target,left,mid-1)
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # step1-find the one target pos
        one_pos = self.binary_find(nums, target)
        
        if one_pos == -1:
            return [-1,-1]
        
        # step2-find start of the target
        start = self.find_first(nums,target,0,one_pos)
        
        # step3-find end of the target
        end = self.find_last(nums,target,one_pos,len(nums)-1)
        
        return [start,end]

def stringToIntegerList(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

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
            line = lines.next()
            target = stringToInt(line)
            
            ret = Solution().searchRange(nums, target)

            out = integerListToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()