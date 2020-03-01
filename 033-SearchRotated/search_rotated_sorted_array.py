import json
class Solution(object):
    """
    Find the pos where rotation happended at, aka original start
    nums - arraylist
    start - start position, include
    end - end position, not included
    """
    def find_split_pos(self, nums, start, end):
        if start >= end:
            return 0
        mid = (start+end)/2
        if mid > 0 and nums[mid] < nums[mid-1]:
            return mid
        left = self.find_split_pos(nums, start, mid)
        if left != 0:
            return left
        right = self.find_split_pos(nums, mid+1, end)
        if right != 0:
            return right
        return 0
    
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
        
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # handle special case
        if len(nums) == 0 or nums is None:
            return -1
        
        if len(nums) == 1:
            return 0 if nums[0]==target else -1
        
        ## step-1: find the pos where rotation happended at
        s_pos = self.find_split_pos(nums,0,len(nums)) 
        
        ## step-2: find the pos using binary search in the two seperate array
        p1 = self.binary_find(nums[:s_pos], target)
        p2 = self.binary_find(nums[s_pos:], target)
        
        if p1 != -1:
            return p1
        if p2 != -1:
            return s_pos+p2
        return -1

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
            
            ret = Solution().search(nums, target)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()