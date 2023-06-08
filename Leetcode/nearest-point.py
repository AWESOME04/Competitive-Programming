class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_distance = float('inf')
        min_index = -1

        for i, point in enumerate(points):
            if point[0] == x or point[1] == y:
                distance = abs(point[0] - x) + abs(point[1] - y)
                if distance < min_distance:
                    min_distance = distance
                    min_index = i

        return min_index
