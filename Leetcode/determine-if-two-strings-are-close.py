class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # count1 = Counter(word1)
        # count2 = Counter(word2)

        # for char in word1:
        #     if char not in word2:
        #         return False
        # if sorted(word1) == sorted(word2):
        #     return True
        # if sorted(count1.values()) == sorted(count2.values()):
        #     return True
        # return False

        # More Optimized Solution -> TC: O(n + klogk) and SC: O(n + k)
        if len(word1) != len(word2):
            return False

        if word1 == word2:
            return True

        c1 = Counter(word1)
        c2 = Counter(word2)

        return all (
            [
                sorted(c1.values()) == sorted(c2.values()),
                set(word1) == set(word2),
            ]
        )
