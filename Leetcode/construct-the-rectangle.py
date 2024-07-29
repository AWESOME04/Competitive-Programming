class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for width in range(isqrt(area), 0, -1):
            if area % width == 0:
                length = area // width 
                return [length, width]
                
        return [area, 1]
