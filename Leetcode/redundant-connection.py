class UnionFind:
    def __init__(self, size):
        self.size = [1] * (size + 1)
        self.root = [i for i in range(size + 1)]

    def find(self, node):
        if node != self.root[node]:
            self.root[node] = self.find(self.root[node])
        return self.root[node]

    def union(self, u, v):
        uroot = self.find(u)
        vroot = self.find(v)

        if uroot == vroot:
            return False

        if uroot != vroot:
            if self.size[uroot] > self.size[vroot]:
                self.root[vroot] = uroot
                self.size[uroot] += self.size[vroot]
            else:
                self.root[vroot] = uroot
                self.size[uroot] += self.size[vroot]
            return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = UnionFind(n)
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
