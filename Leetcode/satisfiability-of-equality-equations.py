class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        root = list(range(26))

        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]
        
        def union(u,v):
            uroot = find(u)
            vroot = find(v)

            root[uroot] = vroot

        for eqn in equations:
            if eqn[1] == "=":
                x, y = ord(eqn[0]) - ord("a"), ord(eqn[3]) - ord("a")
                union(x, y)
        
        for eqn in equations:
            if eqn[1] == "!":
                x, y = ord(eqn[0]) - ord("a"), ord(eqn[3]) - ord("a")
                if find(x) == find(y):
                    return False

        return True
