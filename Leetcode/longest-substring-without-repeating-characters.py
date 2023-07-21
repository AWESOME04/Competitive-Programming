class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left_ptr = 0
        result = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[left_ptr])
                left_ptr += 1
            char_set.add(s[r])
            result = max(result, r - left_ptr + 1)
        return result


