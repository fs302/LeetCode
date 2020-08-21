class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        # Dynamic Programming: F[n] = F[n-1] + F[n-2]

        f = [0, 1, 2]
        
        # inference
        for i in range(3, n+1):
            ans = f[i-1]+f[i-2]
            f.append(ans)
        
        return f[n]

def main():
    ret = Solution().climbStairs(45)
    print(ret)

if __name__ == '__main__':
    main()       