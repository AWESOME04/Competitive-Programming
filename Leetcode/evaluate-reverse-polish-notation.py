class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stack = []
        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                operator1 = stack.pop()
                operator2 = stack.pop()
                if token == "+":
                    stack.append(operator2 + operator1)
                elif token == "-":
                    stack.append(operator2 - operator1)
                elif token == "*":
                    stack.append(operator2 * operator1)
                elif token == "/":
                    stack.append(int(operator2 / operator1))
        return stack[-1]
