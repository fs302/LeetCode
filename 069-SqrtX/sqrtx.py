import math
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        p = x
        while p*p > x:
            p = int((p+x/p)/2)
        return p

num = 1024

if Solution().mySqrt(num) == int(math.sqrt(num)):
    res = Solution().mySqrt(num)
    print("success! {}'s sqrt is {}".format(num, res))
else:
    print("failed.{}'s sqrt is {}, but your answer is {}".format(num, int(math.sqrt(num)), res))