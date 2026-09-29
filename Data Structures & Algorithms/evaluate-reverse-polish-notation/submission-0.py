class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+","-","*","/"]
        

        for token in tokens:
            if token in operators:
                r = stack.pop()
                l = stack.pop()

                match token:
                    case "+": result = l + r
                    case "-": result = l - r
                    case "*": result = l * r
                    case "/": result = int(l / r)
                stack.append(result)

            else:
                stack.append(int(token))
        
        return stack[-1]