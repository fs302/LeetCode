import json

class Solution(object):
    
    def __init__(self):
        self.candidate_str = []

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # counting
        memory = {}
        for k in nums:
            if k not in memory:
                memory[k] = 0
            memory[k] += 1

        # stack
        stack = []
        candidates_str = []
        for k1 in memory:
            stack.append(k1)
            memory[k1] -= 1
            for k2 in memory:
                if k2 >= k1 and memory[k2] > 0:
                    stack.append(k2)
                    k3 = 0-k1-k2
                    memory[k2] -= 1
                    if k3 >= k2 and (k3 in memory and memory[k3] > 0):
                        res = int2dArrayToString([k1,k2,k3])
                        if res not in candidates_str:
                            candidates_str.append(res)
                    stack.pop()
                    memory[k2] += 1
            memory[k1] += 1
            stack.pop()
        
        candidates = []
        
        for st in candidates_str:
            candidates.append(stringToIntegerList(st))
        
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