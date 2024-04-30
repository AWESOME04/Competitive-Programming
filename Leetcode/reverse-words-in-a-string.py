class Solution:
    def reverseWords(self, s: str) -> str:
        # res = s.split(" ")
        # n = len(res)
        # ans = []

        # for i in range(n-1, -1, -1):
        #     if res[i] != "":
        #         ans.append(res[i])

        # return " ".join(ans)

        # TC: O(N)
        # SC: O(N)
        return " ".join(reversed(s.split()))
