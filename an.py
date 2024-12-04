class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operators = {'+', '-', '*', '/'}
        stack = []
        answer = 0
        for token in tokens:
            if token in operators:
                if token == '+':
                    num = stack[-2] + stack[-1]    

                elif token == '-':
                    num = stack[-2] - stack[-1]
                
                elif token == '*':
                    num = stack[-2] * stack[-1]
                
                elif token == '/':
                    num = stack[-2] // stack[-1]

                stack.pop()
                stack.pop()
                stack.append(num)
            else:
                stack.append(token)


        return stack[0]