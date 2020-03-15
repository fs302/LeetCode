import json
class Solution(object):

    def __init__(self):
        self.results = []
    
    def search(self, state, candidates, target):
        if target == 0:
            result = [i for i in state]
            # print(result)
            if result not in self.results:
                self.results.append(result)
            return 
        for i,candidate in enumerate(candidates):
            if i>0 and candidate == candidates[i-1]:
                continue # avoid duplicate position
            if (len(state) == 0 or candidate >= state[-1]) and target-candidate >= 0:
                state.append(candidate)
                new_candidates = []
                once = False
                for d in candidates:
                    if d == candidate and not once:
                        once = True
                        continue
                    new_candidates.append(d)
                self.search(state, new_candidates, target-candidate)
                state.pop()
        return 
    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.results = []
        candidates.sort()
        # print(candidates)
        self.search([], candidates, target)
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
            
            ret = Solution().combinationSum2(candidates, target)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()