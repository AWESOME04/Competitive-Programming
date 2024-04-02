class Solution:
    def reverseVowels(self, s: str) -> str:
        res = list(s)
        l = 0
        r = len(res) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while l < r:
            if res[l] in vowels and res[r] in vowels:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1
            elif res[l] in vowels and res[r] not in vowels:
                r -= 1
            elif res[l] not in vowels and res[r] in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        return "".join(res)
