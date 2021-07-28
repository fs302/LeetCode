class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False
        f = [[False for j in range(l2+1)] for i in range(l1+1)]
        # init
        f[0][0] = True
        # DP: f[i][j] = max(f[i-1][j] & take s1[i], f[i][j-1] & take s2[j])
        for i in range(0, l1+1):
            for j in range(0, l2+1):
                if i == 0 and j == 0:
                    continue
                c1 = c2 = False
                if i > 0:
                    c1 = f[i-1][j] & (s1[i-1] == s3[i+j-1])
                if j > 0:
                    c2 = f[i][j-1] & (s2[j-1] == s3[i+j-1])
                f[i][j] = max(c1, c2)
        return f[l1][l2]
    
if __name__=='__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    s = Solution()
    print(s.isInterleave(s1, s2, s3))