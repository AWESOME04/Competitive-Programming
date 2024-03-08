class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        res = string.ascii_lowercase
        val = {x: x for x in res}

        def find(x):
            if x != val[x]:
                val[x] = find(val[x])
            return val[x]

        for a, b in zip(s1, s2):
            l1, l2 = find(a), find(b)

            if l1 > l2:
                val[l1] = l2
            else:
                val[l2] = l1
                
        return "".join(find(val[x]) for x in baseStr)
