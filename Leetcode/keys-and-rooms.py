class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set([0])

        while queue:
            val = queue.popleft()

            for key in rooms[val]:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)

        if len(visited) == len(rooms):
            return True
        return False
