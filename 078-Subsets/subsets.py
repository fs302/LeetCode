import time
class Solution(object):
    def __init__(self):
        self.results = []
    
    def dfs(self, cur_set, nums):
        out = cur_set[:]
        self.results.append(out)
        for num in nums[:]:
            if len(cur_set) == 0 or num > cur_set[-1]:
                cur_set.append(num)
                nums.remove(num)
                self.dfs(cur_set, nums)
                nums.append(num)
                cur_set.remove(num)
            
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        cur_set = []
        self.dfs(cur_set, nums)
        return self.results

def main():
    s = Solution()
    nums = [1,2,3]
    print(s.subsets(nums))


if __name__ == '__main__':
    main()     