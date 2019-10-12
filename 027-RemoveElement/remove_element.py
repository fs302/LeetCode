
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        j = 0
        while i < len(nums):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
            i += 1
        return j

def main():
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    s = Solution()
    s.removeElement(nums, val)
    print(nums)

if __name__ == '__main__':
    main()