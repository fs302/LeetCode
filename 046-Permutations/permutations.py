class Solution:

    def __init__(self):
        self.res = []

    def search_result(self, avaliable_nums, current_array):
        if len(avaliable_nums) == 0 and len(current_array) > 0:
            self.res.append(current_array.copy())
            return 
        for num in avaliable_nums:
            new_avas = [item for item in avaliable_nums if item != num]
            current_array.append(num)
            self.search_result(new_avas, current_array)
            current_array.remove(num)
        return 

    def permute(self, nums):
        self.res = []
        self.search_result(nums,[])
        return self.res

def main():
    nums = [1,2,3]
    solution = Solution()
    out = solution.permute(nums)
    print(out)
    return 

if __name__ == '__main__':
    main()