class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for t in tokens:
            if t in '-*+/':
                first = stack.pop()
                second = stack.pop()
                if t=='+':
                    stack.append(second+first)
                elif t=='-':
                    stack.append(second-first)
                elif t=='*':
                    stack.append(second*first)
                else:
                    stack.append(int(second/first))
            else:
                stack.append(int(t))
            
            
        return stack.pop()