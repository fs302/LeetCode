class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        sw = x
        inversed_x = 0
        while sw > 0:
            inversed_x = inversed_x * 10 + sw % 10
            sw = sw / 10
        if inversed_x == x:
            return True
        else:
            return False

def stringToInt(input):
    return int(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            x = stringToInt(line)
            
            ret = Solution().isPalindrome(x)

            out = (ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()