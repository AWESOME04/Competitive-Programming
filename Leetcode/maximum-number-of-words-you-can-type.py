class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        for i in text.split(" "):
            if set(brokenLetters).intersection(set(i)) == set():
                count += 1
        return count
