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
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        uf = UnionFind(n)

        for u, v in edges:
            uf.union(u, v)

        return uf.find(source) == uf.find(destination)
