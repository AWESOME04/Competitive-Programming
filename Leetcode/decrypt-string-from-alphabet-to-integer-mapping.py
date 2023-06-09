class Solution:
    def freqAlphabets(self, s: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        result = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                if i < len(s) - 2 and s[i + 2] == '#':
                    result += alphabet[int(s[i:i + 2]) - 1]
                    i += 3
                else:
                    result += alphabet[int(s[i]) - 1]
                    i += 1
            else:
                i += 1

        return result
