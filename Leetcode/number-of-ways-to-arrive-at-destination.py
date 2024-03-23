class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for i, j, k in roads:
            adj_list[i].append((j, k))
            adj_list[j].append((i, k))

        start, end = 0, n-1
        min_dist = {i: [float("inf"), 0] for i in adj_list.keys()}
        min_dist[start] = [0, 1]

        heap = [(0, start)]
        while heap:
            elapsed_time, node = heappop(heap)

            if elapsed_time > min_dist[end][0]:
                break
            for neighbor, time in adj_list[node]:
                if (elapsed_time + time) > min_dist[neighbor][0]:
                    continue

                elif (elapsed_time + time) == min_dist[neighbor][0]:
                    min_dist[neighbor][1] += min_dist[node][1]
                else:
                    min_dist[neighbor][0] = elapsed_time + time
                    min_dist[neighbor][1] = min_dist[node][1]
                    heappush(heap, (elapsed_time + time, neighbor))

        return min_dist[end][1] % (pow(10, 9) + 7)
