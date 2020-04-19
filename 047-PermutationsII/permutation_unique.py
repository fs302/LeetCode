class Solution:

    def __init__(self):
        self.res = []

    def search_result(self, avaliable_nums, current_array):
        if len(avaliable_nums) == 0 and len(current_array) > 0:
            self.res.append(current_array.copy())
            return 
        for i,num in enumerate(avaliable_nums):
            if i > 0 and avaliable_nums[i] == avaliable_nums[i-1]:
                continue
            new_avas = avaliable_nums.copy()
            new_avas.remove(num)
            new_current_array = current_array.copy()
            new_current_array.append(num)
            self.search_result(new_avas, new_current_array)
        return 

    def permuteUnique(self, nums):
        self.res = []
        nums_sorted = sorted(nums)
        self.search_result(nums_sorted,[])
        return self.res

def main():
    nums = [1,1,2,2]
    solution = Solution()
    out = solution.permuteUnique(nums)
    print(out)
    return 

if __name__ == '__main__':
    main()
