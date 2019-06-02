import json
class Solution(object):
    def find_lcp(self, s1, s2):
        lcp = ''
        for i in range(len(s1)):
            if i < len(s2) and s1[i] == s2[i]:
                lcp = lcp + s1[i]
            else:
                break
        return lcp
        
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        cur_lcp = None
        if len(strs) == 0:
            return ''
        for s in strs:
            if cur_lcp is None:
                cur_lcp = s
            else:
                cur_lcp = self.find_lcp(cur_lcp,s)
            if cur_lcp == '':
                break
        return cur_lcp

def stringToStringArray(input):
    return json.loads(input)

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
            
            ret = Solution().longestCommonPrefix(strs)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
