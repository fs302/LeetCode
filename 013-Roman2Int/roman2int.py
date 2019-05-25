class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        S2I = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        num = 0
        lenStr = len(s)
        i = 0
        while i < lenStr:
            if i < lenStr-1 and (s[i+1] in S2I) and (s[i] in S2I) and S2I[s[i]]<S2I[s[i+1]]:
                num += (S2I[s[i+1]]-S2I[s[i]])
                i += 2
                continue
            if s[i] in S2I:
                num += S2I[s[i]]
            i += 1
        return num

def stringToString(input):
    return input.decode('string_escape')

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
            s = stringToString(line)
            
            ret = Solution().romanToInt(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()