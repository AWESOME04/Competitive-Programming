class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        total_shift = 0
        result = []

        for i in range(len(s) - 1, -1, -1):
            total_shift = (total_shift + shifts[i]) % 26
            shifted_index = (alphabet.index(s[i]) + total_shift) % 26
            result.append(alphabet[shifted_index])

        return ''.join(result[::-1])
