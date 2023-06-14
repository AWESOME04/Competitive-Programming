class Solution:
    def similarPairs(self, words: List[str]) -> int:
        d = dict()
        for word in words:
            key = "".join(sorted(set(word)))
            d[key] = d.get(key, 0) + 1

        return sum(v * (v - 1) // 2 for v in d.values())
