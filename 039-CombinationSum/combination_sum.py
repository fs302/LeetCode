import json
class Solution(object):
    def __init__(self):
        self.candidates = []
        self.results = []
    
    def search(self, state, target):
        if target == 0:
            result = [i for i in state]
            self.results.append(result)
            # print(result)
            return 
        for candidate in self.candidates:
            if len(state) == 0 or candidate >= state[-1]: # important condition
                if target-candidate >= 0:
                    state.append(candidate)
                    self.search(state, target-candidate)
                    state.pop()
        return 
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.candidates = candidates
        self.results = []
        self.search([], target)
        return self.results
        

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
            candidates = stringToIntegerList(line)
            line = lines.next()
            target = stringToInt(line)
            
            ret = Solution().combinationSum(candidates, target)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()