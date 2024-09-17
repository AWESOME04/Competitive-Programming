class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        additions = [0] * n
        increase = [0] * n

        for u, v in relations:
            graph[u-1].append(v-1)
            additions[v-1] += 1

        queue = deque([i for i in range(n) if additions[i] == 0])
        ans = 0

        while queue:
            for i in range(len(queue)):
                curr = queue.popleft()
                ans = max(ans, time[curr])

                for neighbour in graph[curr]:
                    additions[neighbour] -= 1
                    increase[neighbour] = max(increase[neighbour], time[curr])

                    if additions[neighbour] == 0:
                        queue.append(neighbour)
                        time[neighbour] += increase[neighbour]

        return ans
