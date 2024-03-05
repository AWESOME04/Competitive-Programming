class UnionFind:
    def __init__(self, size):
        self.size = [1] * size
        self.root = [i for i in range(size)]
        
    def find(self, node):
        if node != self.root[node]:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, u, v):
        uroot = self.find(u)
        vroot = self.find(v)

        if uroot != vroot:
            if self.size[uroot] > self.size[vroot]:
                self.root[vroot] = uroot
                self.size[uroot] += self.size[vroot]
            elif self.size[uroot] < self.size[vroot]:
                self.root[uroot] = vroot
                self.size[vroot] += self.size[uroot]
            else:
                self.root[vroot] = uroot
                self.size[uroot] += self.size[vroot]

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        components = n

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    if uf.find(i) != uf.find(j):
                        uf.union(i, j)
                        components -= 1
                        
        return components
