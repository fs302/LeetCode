class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1] # put -1 to label begin pos
        max_len = 0
        BEGIN = '('
        END = ')'
        for i,ch in enumerate(s):
            if ch == BEGIN:
                stack.append(i)
            elif ch == END:
                stack.pop()
                if len(stack) == 0:
                    stack.append(i) # let i as another begin
                else:
                    max_len = max(max_len, i - stack[-1])
        return max_len

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
            
            ret = Solution().longestValidParentheses(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()