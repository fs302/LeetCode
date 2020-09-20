class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # naive solution
        if nums is None or len(nums)==0:
            return nums
        counter = [0,0,0] # counter for 0,1,2
        for num in nums:
            counter[num] += 1
        pos = 0
        for i,cnt in enumerate(counter):
            for j in range(cnt):
                nums[pos] = i
                pos += 1
        return nums
        
def main():
    nums = [2,2,1,1,0,2] 
    ret = Solution().sortColors(nums)
    print(ret)

if __name__ == '__main__':
    main()     