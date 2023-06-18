from typing import List

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        common_chars = list(words[0])  
        for word in words[1:]:
            current_chars = list(word)
            temp = []
            for char in common_chars:
                if char in current_chars:
                    temp.append(char)
                    current_chars.remove(char)
            common_chars = temp

        return common_chars
