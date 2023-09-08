class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        for i in path.split("/"):

            if i == "..":
                if stack:
                    stack.pop()
            elif i == "." or i == '':
                continue
            else:
                stack.append(i)

        res = "/" + "/".join(stack)
        return res
