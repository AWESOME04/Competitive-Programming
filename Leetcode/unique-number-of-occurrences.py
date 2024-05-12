class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)

        if len(set(count.values())) == len(count.values()):
            return True
        return False

    # TC: O(n)
    # SC: O(n)
