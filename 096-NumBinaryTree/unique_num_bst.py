class Solution:
    def numTrees(self, n: int) -> int:
        # recursion DP
        f = [1, 1] # f[0]=1, f[1]=1
        if n > 1:
            for i in range(2, n+1):
                tmp = 0
                for k in range(i):
                    tmp += f[k]*f[i-1-k]
                f.append(tmp)
        return f[n]
        # another solution: Catalan Number