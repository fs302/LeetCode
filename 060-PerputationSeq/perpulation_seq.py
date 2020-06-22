import math 
class Solution(object):

    def solve(self, candidates, k):
        if len(candidates) == 1:
            return str(candidates[0])
        l = len(candidates)
        th = math.factorial(l-1)
        index = (k-1) // th         # get the position of the current number
        head = candidates[index]
        candidates.pop(index)
        k_next = k % th             # modify the next k
        return str(head)+self.solve(candidates, k_next)

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        candidates = [i for i in range(1,n+1)]

        return self.solve(candidates, k)

def main():
    n = 9
    k = 10 
    s = Solution()
    print(k, s.getPermutation(n,k))

if __name__ == '__main__':
    main()