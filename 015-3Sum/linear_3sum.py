import json

class Solution(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    
        candidates = []
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if i == 0 or (sorted_nums[i] != sorted_nums[i-1]):
                k1 = sorted_nums[i] # first number
                head = i+1
                tail = len(sorted_nums)-1
                while head < tail:  # find second and third
                    if sorted_nums[head]+sorted_nums[tail]==-k1:
                        k2 = sorted_nums[head]
                        k3 = sorted_nums[tail]
                        candidates.append([k1,k2,k3])
                        while head < tail and sorted_nums[head+1]==sorted_nums[head]:
                            head += 1
                        while head < tail and sorted_nums[tail-1]==sorted_nums[tail]:
                            tail -= 1
                        head += 1
                        tail -= 1
                    else:
                        if sorted_nums[head]+sorted_nums[tail]<-k1:
                            head += 1
                        else:
                            tail -= 1
        
        return candidates
    
    
def stringToIntegerList(input):
    return json.loads(input)

def int2dArrayToString(input):
    return json.dumps(input)

def stringToIntegerList(input):
    return json.loads(input)

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
            
            ret = Solution().threeSum(nums)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()