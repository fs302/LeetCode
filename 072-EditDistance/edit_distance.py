class Solution(object):

    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # extreme-cases
        if word1 == word2:
            return 0
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        
        # init
        m, n = len(word1), len(word2)
        f = [[-1 for j in range(n+1)] for i in range(m+1)]

        for i in range(m+1):
            f[i][0] = i
        for j in range(n+1):
            f[0][j] = j

        # DP, f[i][j] means the minimum step needed for word1[:i] and word2[:j] to be consistent.
        # the key operator is to check word1[i] and word2[j]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    f[i][j] = f[i-1][j-1]
                else:
                    f[i][j] = min(f[i-1][j-1],min(f[i][j-1],f[i-1][j])) + 1
        
        return f[m][n]
        
def main():
    word1 = 'intention'
    word2 = 'execution'
    ret = Solution().minDistance(word1,word2)
    print(ret)

if __name__ == '__main__':
    main()       