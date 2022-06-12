class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '+':
                firstOperand = stack.pop()
                secondOperand = stack.pop()
                stack.append(secondOperand + firstOperand)
            elif token == '-':
                firstOperand = stack.pop()
                secondOperand = stack.pop()
                stack.append(secondOperand - firstOperand)
            elif token == '*':
                firstOperand = stack.pop()
                secondOperand = stack.pop()
                stack.append(secondOperand * firstOperand)
            elif token == '/':
                firstOperand = stack.pop()
                secondOperand = stack.pop()
                stack.append(math.trunc(secondOperand / firstOperand))
            else:
                stack.append(int(token))
        return stack.pop()