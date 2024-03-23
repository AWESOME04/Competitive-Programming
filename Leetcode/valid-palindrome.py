class Solution:
    def isPalindrome(self, s: str) -> bool:
        # res = "".join(c.lower() for c in s if c.isalnum())
        # return res == res[::-1]

        # Using two pointers
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True
    
