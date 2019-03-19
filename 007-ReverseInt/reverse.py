
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x>0 else -1
        res = 0
        x = abs(x)
        while x>0:
            digit = x % 10
            res = res * 10 + digit
            x /= 10
        if res>=2**31:
            return 0
        return sign * res
            
def main():
    x = 126791878090998
    s = Solution()
    print x,s.reverse(x)

main()