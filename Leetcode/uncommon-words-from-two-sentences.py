class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_words = s1.split()
        s2_words = s2.split()

        counter = Counter(s1_words + s2_words)
        
        return [word for word, count in counter.items() if count == 1]
