class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        combined_list = []
        i = 0 
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i]<nums2[j]:
                combined_list.append(nums1[i])
                i += 1
            else:
                combined_list.append(nums2[j])
                j += 1
        if i < len(nums1):
            combined_list.extend(nums1[i:])
        if j < len(nums2):
            combined_list.extend(nums2[j:])
        size = len(combined_list)
        res = 0
        if size % 2 == 1:
            res = combined_list[int(size/2)]
        else:
            res = (combined_list[int(size/2)-1]+combined_list[int(size/2)])/2.0
        return res

if __name__ == "__main__":
    s = Solution()
    array_1 = sorted([1,4])
    array_2 = sorted([2,3,4,5,6,7,8])
    print 'array 1',array_1
    print 'array 2:',array_2
    print 'result:',s.findMedianSortedArrays(array_1, array_2)