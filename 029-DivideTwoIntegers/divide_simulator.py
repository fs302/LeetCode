class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if dividend < 0:
            dividend = -dividend
            sign = -sign
        if divisor < 0:
            divisor = -divisor
            sign = -sign
        res = 0
        agent = divisor
        unit = 1
        # using: bit operator and add operator
        while dividend >= divisor:
            if dividend >= agent:
                dividend -= agent
                res += unit
                agent = agent << 1
                unit = unit << 1
            else:
                agent = agent >> 1
                unit = unit >> 1
        res = res * sign
        return min(max(-2147483648,res),2147483647)
            

def stringToInt(input):
    return int(input)

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
            dividend = stringToInt(line)
            line = lines.next()
            divisor = stringToInt(line)
            
            ret = Solution().divide(dividend, divisor)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()