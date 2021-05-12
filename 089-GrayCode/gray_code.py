class Solution:
    def __init__(self):
        self.res = []
        self.answer = []
        self.visited = {}
        self.finish = False
    
    def dfs(self, status, depth, n):
        if depth == (1 << n):
            self.finish = True
            self.answer = self.res.copy()
            return 
        for i in range(n):
            new_status = status ^ (1 << i)
            if (new_status not in self.visited or not self.visited[new_status]) and not self.finish:
                self.visited[new_status] = True
                self.res.append(new_status)
                self.dfs(new_status, depth+1, n)
                self.res.pop()
                self.visited[new_status] = False
        

    def grayCode(self, n: int) -> List[int]:
        self.res.append(0)
        self.visited[0] = True
        self.finish = False
        self.dfs(0, 1, n)
        return self.answer