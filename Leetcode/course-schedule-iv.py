class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # graph = defaultdict(list)

        # for start, dest in prerequisites:
        #     graph[start].append(dest)

        # def hasPath(start, dest):
        #     minHeap = [(0, start)]
        #     visited = set()

        #     while minHeap:
        #         cost, node = heapq.heappop(minHeap)
        #         if node in visited:
        #             continue
        #         visited.add(node)

        #         if node == dest:
        #             return True

        #         for neighbour in graph[node]:
        #             if neighbour not in visited:
        #                 heapq.heappush(minHeap, (cost + 1, neighbour))
        #     return False

        # res = []

        # for start, dest in queries:
        #     res.append(hasPath(start, dest))
        # return res

        # Using Floyd Warshall Algorithm
        dist = [[float("inf")] * numCourses for _ in range(numCourses)]

        for i in range(numCourses):
            dist[i][i] = 0

        for src, dest in prerequisites:
            dist[src][dest] = 1

        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        res = []
        for a, b in queries:
            if dist[a][b] != float("inf"):
                res.append(True)
            else:
                res.append(False)
        
        return res
