class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = Counter(words)
        heap = []
        res = []

        for word, count in freq.items():
            heapq.heappush(heap, (-count, word))

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
