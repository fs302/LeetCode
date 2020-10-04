import time
class Solution(object):
    def __init__(self):
        self.n = None
        self.memory = dict()
    
    def dfs(self, bottom, energy):
        # optimize for memory, save search time for duplicate results
        if (bottom,energy) in self.memory:
            return self.memory[(bottom,energy)]
        # ending search
        if energy == 1:
            return [[bottom]]
        results = []
        for v in range(bottom, self.n):
            tail_list = self.dfs(v+1, energy-1)
            for result in tail_list:
                results.append([bottom]+result)
        self.memory[(bottom,energy)] = results
        return results
        
    def memory_search(self, n, k):
        self.n = n 
        self.memory = dict()
        results = []
        for i in range(1, n+1-k+1):
            combinations = self.dfs(i, k)
            if combinations is not None:
                results = results + combinations
        return results

    def dp(self, n, k):
        
        # initialize: F[n,1]
        tmp = []
        pre_k_results = {}
        for i in range(1,n+1):
            tmp.append([i])
            pre_k_results[i] = tmp.copy()
        
        results = pre_k_results
        # F[n,k] = F[n-1,k] + (item + [n] for item in F[n-1, k-1])
        for col in range(2,k+1):
            cur_k_results = {}
            for row in range(col,n-k+col+1):
                cur_results = []
                # Part1: F[n-1, k]
                if row > col:
                    cur_results = cur_results + pre_n_results
                # Part2: (item + [n] for item in F[n-1, k-1])
                for item in pre_k_results[row-1]:
                    cur_results.append(item+[row])
                pre_n_results = cur_results
                cur_k_results[row] = cur_results
            pre_k_results = cur_k_results
            results = cur_k_results
        
        return results[n]

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        results = self.memory_search(n, k)
        # results = self.dp(n, k)
        return results

def main():

    # n, k = 4, 1
    # start = time.time()
    # ret2 = Solution().dp(n, k)
    # end = time.time()
    # dp_time = round((end-start)*1000*1000,2) 
    # print(ret2, dp_time)

    ## time consume test
    for n in range(5,10):
        for k in range(2,n):
            start = time.time()
            ret1 = Solution().memory_search(n, k)
            end = time.time()
            memory_search_time = round((end-start)*1000*1000,2)
            start = time.time()
            ret2 = Solution().dp(n, k)
            end = time.time()
            dp_time = round((end-start)*1000*1000,2)
            print("n={n},k={k} memory_search consume:{memory_search_time}ms, dp consume:{dp_time}ms".format(**locals()))


if __name__ == '__main__':
    main()     