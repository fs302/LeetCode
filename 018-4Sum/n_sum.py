import json

class Solution(object):
    def nSum(self, sorted_nums, target, n):
        if n == 1:
            if target in sorted_nums:
                return [[target]]
            else:
                return []
        if len(sorted_nums) < n:
            return []
        candidates = []
        if n == 2: #solving 2-sum problem
            l, r = 0, len(sorted_nums)-1
            while l < r:
                s = sorted_nums[l] + sorted_nums[r]
                if s == target:
                    candidates.append([sorted_nums[l],sorted_nums[r]])
                    l += 1
                    while l < r and sorted_nums[l] == sorted_nums[l-1]:
                        l += 1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(len(sorted_nums)-n+1):
                if i > 0 and sorted_nums[i] == sorted_nums[i-1]: # solving duplicate vectors
                    continue
                v = sorted_nums[i]
                left_nums = sorted_nums[i+1:]
                left_result = self.nSum(left_nums, target-v, n-1) # deep first search
                for item in left_result:
                    item.insert(0,v)
                    candidates.append(item)
        # print 'n:', n, ',target:',target, sorted_nums, candidates
        return candidates

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        sorted_nums = sorted(nums)
        return self.nSum(sorted_nums, target, 4)

def stringToIntegerList(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

def int2dArrayToString(input):
    return json.dumps(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            nums = stringToIntegerList(line)
            line = lines.next()
            target = stringToInt(line)
            
            ret = Solution().fourSum(nums, target)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()