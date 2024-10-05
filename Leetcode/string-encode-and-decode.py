class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for char in strs:
            res += str(len(char)) + "#" + char
        
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return res
