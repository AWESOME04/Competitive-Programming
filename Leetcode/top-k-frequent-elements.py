class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = []
        
        # freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))
        # res = list(freq.keys())[:k]
        # return res

        ans = freq.most_common(k)
        for key, val in ans:
            res.append(key)
        
        return res

        # TC: O(n + mlogk)
        # SC: O(m + k)
