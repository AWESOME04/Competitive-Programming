class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        res = 0

        for i in range(len(points) - 1 ):
            res = max(res, points[i + 1][0] - points[i][0])

        return res
