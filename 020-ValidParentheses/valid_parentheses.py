import sys

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        v_map = {'(':1,')':-1,'{':2,'}':-2,'[':3,']':-3}
        flag = True
        stack = []
        for k in s:
            value = v_map[k]
            if value > 0:
                stack.append(value)
            else:
                if len(stack) > 0 and value + stack[-1] == 0:
                    stack.pop()
                else:
                    flag = False
        if len(stack) != 0:
            flag = False
        return flag

def stringToString(input):
    return input[1:-1].decode('string_escape')

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
            
            ret = Solution().isValid(s)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()