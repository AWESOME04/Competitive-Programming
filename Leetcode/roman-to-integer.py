class Solution:
    def romanToInt(self, s: str) -> int:
        rom_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        res = 0

        for i in range(len(s)):
            if i < len(s) - 1 and rom_num[s[i]] < rom_num[s[i+1]]:
                res -= rom_num[s[i]]
            else:
                res += rom_num[s[i]]

        return res

        # Time Complexity: O(N)
        # Space Complexity: O(1)
