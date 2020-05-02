class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n == 1 or x == 0:
            return x
        if n < 0:
            return 1.0 / self.myPow(x, -n)
        # Fast Pow
        half = self.myPow(x, n/2)
        if n % 2 == 0:
            return half * half
        else:
            return x * half * half

def stringToDouble(input):
    return float(input)

def stringToInt(input):
    return int(input)

def doubleToString(input):
    if input is None:
        input = 0
    return "%.5f" % input

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            x = stringToDouble(line)
            line = lines.next()
            n = stringToInt(line)
            
            ret = Solution().myPow(x, n)

            out = doubleToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()