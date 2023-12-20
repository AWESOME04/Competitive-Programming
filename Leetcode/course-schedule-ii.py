class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = [[] for _ in range(numCourses)]

        for source, destination in prerequisites:
            adj_list[source].append(destination)

        queue = []
        valid, cycle = set(), set()

        def dfs(source):
            if source in cycle:
                return False
            if source in valid:
                return True

            cycle.add(source)

            for destination in adj_list[source]:
                if not dfs(destination):
                    return False
                
            cycle.remove(source)
            valid.add(source)
            queue.append(source)

            return True

        for source in range(numCourses):
            if not dfs(source):
                return []
            
        return queue
