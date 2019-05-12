class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Naive Solution-TLE
        """
        cur_max = 0
        for i in range(len(height)):
        	for j in range(i):
        		candidate = (i-j)*min(height[i],height[j])
        		if cur_max < candidate:
        			cur_max = candidate	
        """
        # Pointer process
        i, j = 0, len(height)-1
        cur_max = (j-i)*min(height[i],height[j])
        while i<j:
        	if height[i] < height[j]:
        		i += 1
        	else:
        		j -= 1
        	candidate = (j-i)*min(height[i],height[j])
        	if cur_max < candidate:
        		cur_max = candidate
        return cur_max

def main():
	s = Solution()
	height = [1,8,6,2,5,4,8,3,7]
	# height = [1,9,6,2,5,4,8,9,7]
	# height = [2,3,10,5,7,8,9]
	print height, s.maxArea(height)

if __name__=='__main__':
	main()