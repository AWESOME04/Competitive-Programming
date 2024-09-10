class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(list)

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        leaves = deque()
        edge_count = {}

        for node in graph:
            if len(graph[node]) == 1:
                leaves.append(node)
            edge_count[node] = len(graph[node])
        
        while n > 2:
            level = len(leaves)
            n -= level

            for _ in range(level):    
                node = leaves.popleft() 
                for neighbor in graph[node]:
                    edge_count[neighbor] -= 1
                    if edge_count[neighbor] == 1:
                        leaves.append(neighbor)

        return leaves
