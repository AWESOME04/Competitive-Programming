class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # l,r,count, res = 0,0,0,0
        # data = set()
        # while r<len(s):
        #     if s[r] not in data:
        #         data.add(s[r])
        #         count+=1
        #         r+=1
        #     else:
        #         data.remove(s[l])
        #         l+=1
        #         count-=1
        #     res = max(res, count)
        # return res


        # Sliding window approach
        # curr_set = set()
        # left_ptr = 0
        # res = 0

        # for r in range(len(s)):
        #     while s[r] in curr_set:
        #         curr_set.remove(s[left_ptr])
        #         left_ptr += 1
        #     curr_set.add(s[r])

        #     res = max(res, r - left_ptr + 1)
        # return res

        # Dynamic Sliding window
    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            n = len(s)
            if len(set(s)) == 1:
                return 1
    
            seen = {}
            max_len = 0
            start = 0
    
            for end in range(n):
                if s[end] in seen and seen[s[end]] >= start:
                    start = seen[s[end]] + 1
                seen[s[end]] = end
                max_len = max(max_len, end - start + 1)
            return max_len
    
