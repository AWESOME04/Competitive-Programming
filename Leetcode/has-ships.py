class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
def hasShips(bottom_left: Point, top_right: Point) -> int:
    # Base cases
    if bottom_left.x > top_right.x or bottom_left.y > top_right.y:
        return 0
        
    if not hasShips(bottom_left, top_right):
        return 0
        
    if bottom_left.x == top_right.x and bottom_left.y == top_right.y:
        return 1
        
    # middle points
    mid_x = (bottom_left.x + top_right.x) // 2
    mid_y = (bottom_left.y + top_right.y) // 2
        
    count = 0
    
    # 4 Quadrants
    count = 0

    # Bottom-left quadrant (Area 3)
    count += countShips(
        Point(bottom_left.x, bottom_left.y),
        Point(mid_x, mid_y)
    )
    
    # Bottom-right quadrant (Area 4)
    count += countShips(
        Point(mid_x + 1, bottom_left.y),
        Point(top_right.x, mid_y)
    )
    
    # Top-left quadrant (Area 1)
    count += countShips(
        Point(bottom_left.x, mid_y + 1),
        Point(mid_x, top_right.y)
    )
    
    
    # Top-right quadrant (Area 2)
    count += countShips(
        Point(mid_x + 1, mid_y + 1),
        Point(top_right.x, top_right.y)
    )
    
    return count
