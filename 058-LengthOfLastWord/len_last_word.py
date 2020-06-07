## Sample input: "Hello World", Return 5
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return 0
        return len(s.strip().split(' ')[-1])

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
            s = stringToString(line)
            
            ret = Solution().lengthOfLastWord(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()