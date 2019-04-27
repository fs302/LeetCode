class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        clean_str = str.strip(' ')
        if len(clean_str) == 0:
            return 0
        value = 0
        sign = 1
        if clean_str[0]=='-':
            sign = -1
            clean_str = clean_str[1:]
        elif clean_str[0]=='+':
            sign = 1
            clean_str = clean_str[1:]
        for char in clean_str:
            if char in ['0','1','2','3','4','5','6','7','8','9']:
                value = value * 10 + int(char)
            else:
                break
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        value = value * sign
        if value > INT_MAX:
            value = INT_MAX
        if value < INT_MIN:
            value = INT_MIN
        return value

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
            str = stringToString(line)
            
            ret = Solution().myAtoi(str)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()