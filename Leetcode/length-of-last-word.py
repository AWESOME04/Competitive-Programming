class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        rem_ws = s.strip()

        s_list = rem_ws.split(" ")
        return len(s_list[-1])
