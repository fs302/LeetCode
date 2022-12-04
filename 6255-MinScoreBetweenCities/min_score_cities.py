class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = {}
        for road in roads:
            u, v, e = road[0], road[1], road[2]
            if u not in adj:
                adj[u] = {}
            if v not in adj:
                adj[v] = {}
            adj[u][v] = e
            adj[v][u] = e
        
        # bfs: TLE in Python, pass in C++
        # min_dis = 10**5+1
        # visited = {}
        # queue = [1]
        # while len(queue) > 0:
        #     u = queue.pop(0)
        #     visited[u] = 1
        #     for v in adj[u]:
        #         min_dis = min(min_dis, adj[u][v])
        #         if v not in visited:
        #             queue.append(v)

        # dfs
        # self.visited = {}
        # self.min_dis = 10**5+1
        # def dfs(node):
        #     if node not in self.visited:
        #         self.visited[node] = 1
        #         for v in adj[node]:
        #             self.min_dis = min(self.min_dis, adj[node][v])
        #             dfs(v)
        # dfs(1)

        # union
        self.min_dis = 10**5+1
        uset = Union(n+1)
        for road in roads:
            u, v, e = road[0], road[1], road[2]
            uset.union(u, v)
        for road in roads:
            u, v, e = road[0], road[1], road[2]
            #print(u, uset.is_connected(u, 1))
            if uset.is_connected(u, 1):
                self.min_dis = min(self.min_dis, e)

        return self.min_dis

class Union:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x = self.find(x) # find father x->px->ppx...
        y = self.find(y) # find father y->py->ppy...
        if x == y:
            return 
        if self.p[x] < self.p[y]:
            self.p[y] = self.p[x] # small is father
        else:
            self.p[x] = self.p[y]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)