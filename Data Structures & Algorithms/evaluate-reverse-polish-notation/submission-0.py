class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = ["+", "-", "*", "/"]
        stack = []
        result = 0
        for num in tokens:
            if num not in operands:
                stack.append(num)
            else:
                if num == "+":
                    x1 = int(stack[-1])
                    stack.pop()
                    x2 = int(stack[-1])
                    stack.pop()
                    stack.append(x1 + x2)
                elif num == "-":
                    x1 = int(stack[-1])
                    stack.pop()
                    x2 = int(stack[-1])
                    stack.pop()
                    stack.append(x2-x1)
                elif num == "*":
                    x1 = int(stack[-1])
                    stack.pop()
                    x2 = int(stack[-1])
                    stack.pop()
                    stack.append(x1 * x2)
                elif num == "/":
                    x1 = int(stack[-1])
                    stack.pop()
                    x2 = int(stack[-1])
                    stack.pop()
                    stack.append(x2/x1)
        return int(stack[-1])
