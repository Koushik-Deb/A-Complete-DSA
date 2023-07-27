class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        inside = ['(','{','[']
        dt = {
            '(':')',
            '{':'}',
            '[':']'
        }
        
        for item in s:
            if item in inside:
                stack.append(item)  
            elif stack and dt[stack[-1]]==item:
                stack.pop()
            else:
                return False
        
        return len(stack)==0
                