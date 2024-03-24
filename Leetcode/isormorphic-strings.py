class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

        # ALT
        # m1, m2 = [], []

        # for i in s:
        #     m1.append(s.index(i))

        # for i in t:
        #     m2.append(t.index(i))

        # return m1 == m2
