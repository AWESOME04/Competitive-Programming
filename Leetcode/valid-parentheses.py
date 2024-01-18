class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False
            
        if len(stack) == 0:
            return True
        return False

        # Time Complexity: O(N)
        # Space Complexity: O(N)


        # ALT Solution
        # stack = []
        
        # for char in s:
        #     if char == "(":
        #         stack.append(")")
        #     elif char == "{":
        #         stack.append("}")
        #     elif char == "[":
        #         stack.append("]")
        #     elif not stack or stack.pop() != char:
        #         return False
            
        # if len(stack) == 0:
        #     return True
        # return False
