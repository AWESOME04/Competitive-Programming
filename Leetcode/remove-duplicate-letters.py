class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        n = len(s)
        stack = []
        last_occurrence = {}
        visited = set()

        for i in range(n):
            last_occurrence[s[i]] = i
        for i in range(n):
            if s[i] in visited:
                continue
            while stack and s[i] < stack[-1] and last_occurrence[stack[-1]] > i:
                visited.remove(stack.pop())
            stack.append(s[i])
            visited.add(s[i])

        return "".join(stack)
