class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        terminal node - no outgoing edges
        safe node - leads to terminal node or other node
        use a hashmap to det the safe and unsafe states
        """
        n = len(graph)
        safe = {}
        safe_nodes = []

        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False

            for neighbour in graph[i]:
                if not dfs(neighbour):
                    return False
            safe[i] = True
            return True

        for i in range(n):
            if dfs(i):
                safe_nodes.append(i)
        return safe_nodes
