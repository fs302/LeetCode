class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # naive solution
        ## remember which number have more than 2 repeator, and make it 2.
        
        # inplace solution
        ## two-pointers i: the natural passing, pos: the final anchor
        
        pos = 0
        window = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                window = 1
            else:
                window += 1
            if window < 3:
                nums[pos] = nums[i]
                pos += 1
        return pos
                
def main():
    s = Solution()
    nums = [1,1,2,2,2,3]
    ret = s.removeDuplicates(nums)
    print(nums[:ret])


if __name__ == '__main__':
    main()    