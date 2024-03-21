class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.size = [1]* size

    def find(self, node):
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]
        
    def union(self, x, y):
        xroot, yroot = self.find(x), self.find(y)

        if xroot != yroot:
            if self.size[xroot] > self.size[yroot]:
                self.root[yroot] = xroot
                self.size[xroot] += self.size[yroot]
            else:
                self.root[xroot] = yroot
                self.size[yroot] += self.size[xroot]
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        emailToAcc = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in emailToAcc:
                    uf.union(i, emailToAcc[e])
                else:
                    emailToAcc[e] = i
        
        emailGrp = defaultdict(list)

        for e, i in emailToAcc.items():
            leader = uf.find(i)
            emailGrp[leader].append(e)
        
        res = []
        for i, e in emailGrp.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGrp[i]))

        return res
