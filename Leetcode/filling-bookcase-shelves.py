class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_char = list(words[0])
        for word in words[1:]:
            current_char = list(word)
            temp = []

            for char in common_char:
                if char in current_char:
                    temp.append(char)
                    current_char.remove(char)
            common_char = temp

        return common_char
