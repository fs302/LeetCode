class Solution(object):

    def partial_match_table_god(self, pattern_st):
        p = [0]
        j = 0
        for i in range(1,len(pattern_st)):
            while j > 0 and pattern_st[i] != pattern_st[j]:
                j = p[j-1]
            if pattern_st[i] == pattern_st[j]:
                j += 1
            p.append(j)
        return p
        
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle is None or len(needle)==0:
            return 0
        p = self.partial_match_table_god(needle)
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = p[j-1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i-j+1
        return -1

def stringToString(input):
    return input[1:-1].decode('string_escape')

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
            haystack = stringToString(line)
            line = lines.next()
            needle = stringToString(line)
            
            ret = Solution().strStr(haystack, needle)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()