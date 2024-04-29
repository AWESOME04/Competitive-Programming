class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # n = len(candies)
        # result = []
        # maxx = max(candies)
        
        # l = 0
        # while l < n:
        #     if candies[l] + extraCandies >= maxx:
        #         result.append(True)
        #         l += 1
        #     else:
        #         result.append(False)
        #         l += 1
        # return result

        return [c + extraCandies >= max(candies) for c in candies]

  # TC: O(N)
  # SC: O(N)
