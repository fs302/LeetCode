import time
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums)-1

        while (l <= r):
            m = l + (r-l)//2

            if nums[m] == target:
                return True 
            
            # since nums[m] != target, if nums[l]==nums[m], it can be skiped
            while nums[l] == nums[m] and l < m:
                l += 1 
            
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]: # First part [l,m) is incresing, we can find anwser
                    r = m - 1
                else:                           # Answer lies in Second part
                    l = m + 1 
            elif nums[l] > nums[m]:
                if nums[m] < target <= nums[r]: # Second part (m,r] is incresing, we can find answer
                    l = m + 1
                else:
                    r = m - 1                   # Elsewise

        return False
        

def main():
    s = Solution()
    nums = [1,3,4]
    print(s.search(nums, 4))


if __name__ == '__main__':
    main()     