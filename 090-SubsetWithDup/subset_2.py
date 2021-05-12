class Solution:
    def __init__(self):
        self.res = []

    def search(self, link, cur_map, quota):
        if quota == 0:
            return 
        for k in cur_map.keys():
            if cur_map[k] > 0 \
                and (len(link) == 0 or k >= link[-1]):
                cur_map[k] -= 1
                link.append(k)
                self.res.append(link[:])
                self.search(link, cur_map, quota-1)
                link.pop()
                cur_map[k] += 1
        return

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # quota-statistics
        st_map = {}
        for num in nums:
            if num not in st_map:
                st_map[num] = 0
            st_map[num] += 1
        
        # search for candidates
        link = []
        self.res.append(link)
        self.search(link, st_map, len(nums))

        return self.res

