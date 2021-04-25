from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 1.easy-implement

        # t_nums1 = nums1[:m]
        # t_nums2 = nums2[:n]
        # i , j, k = 0, 0, 0
        # while i < len(t_nums1) and j < len(t_nums2):
        #     if t_nums1[i] < t_nums2[j]:
        #         nums1[k] = t_nums1[i]
        #         i += 1
        #         k += 1
        #     else:
        #         nums1[k] = t_nums2[j]
        #         j += 1
        #         k += 1
        # while i < len(t_nums1):
        #     nums1[k] = t_nums1[i]
        #     i += 1
        #     k += 1
        # while j < len(t_nums2):
        #     nums1[k] = t_nums2[j]
        #     j += 1
        #     k += 1
        
        # 2.sort-trick
        for i in range(m, m+n):
            nums1[i] = nums2[i-m]
        nums1.sort()

if __name__ == '__main__':
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [1,4,5]
    n = 3
    s = Solution()
    s.merge(nums1, m, nums2, n)
    print(nums1)