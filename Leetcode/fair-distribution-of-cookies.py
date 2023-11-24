class Solution:
    def __init__(self):
        self.unfairness = float("inf")
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        children = [0]*k
        def backtrack(child,i):
            if i == len(cookies):
                potential = max(child)
                self.unfairness = min(potential,self.unfairness)
                return
            for j in range(len(child)):
                child[j]+=cookies[i]
                if cookies[i] < self.unfairness:
                    backtrack(child,i+1)
                child[j]-=cookies[i]

        backtrack(children,0)
        return self.unfairness
