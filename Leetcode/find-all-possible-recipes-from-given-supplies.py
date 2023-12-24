class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for r, ing in zip(recipes, ingredients):
            indegree[r] = len(ing)

            for i in ing:
                graph[i].append(r)

        queue = deque(supplies)
        visited = []
        ans = []

        while queue:
            sup = queue.popleft()

            if sup in recipes:
                ans.append(sup)
            
            for r in graph[sup]:
                indegree[r] -= 1
                if indegree[r] == 0:
                    queue.append(r)
                    
        return ans
