import json
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        for st in strs:
            sorted_st = ''.join(sorted(st))
            if sorted_st not in hashmap:
                hashmap[sorted_st] = []
            hashmap[sorted_st].append(st)
        output = []
        for key,group in hashmap.items():
            output.append(group)
        return output
            

def stringToStringArray(input):
    return json.loads(input)

def string2dArrayToString(input):
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
            strs = stringToStringArray(line)
            
            ret = Solution().groupAnagrams(strs)

            out = string2dArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()