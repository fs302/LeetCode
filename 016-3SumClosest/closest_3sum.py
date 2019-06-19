import sys
import json

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        candidates = []
        min_diff = sys.maxint
        best = target
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if i == 0 or (sorted_nums[i] != sorted_nums[i-1]):
                k1 = sorted_nums[i] # first number
                head = i+1
                tail = len(sorted_nums)-1
                while head < tail:  # find second and third
                    if abs(k1+sorted_nums[head]+sorted_nums[tail]-target)<min_diff:
                        min_diff = abs(k1+sorted_nums[head]+sorted_nums[tail]-target)
                        best = k1+sorted_nums[head]+sorted_nums[tail]
                    if sorted_nums[head]+sorted_nums[tail]+k1<target:
                        head += 1
                    else:
                        tail -= 1
        return best

def stringToIntegerList(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

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
            
            ret = Solution().threeSumClosest(nums, target)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()