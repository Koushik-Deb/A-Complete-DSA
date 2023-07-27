class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = list(zip(position, speed))
        zipped.sort(reverse=True)
        stack = []
        
        for p,s in zipped:
            time = (target-p)/s
            
            if stack and stack[-1]>=time:
                continue
            
            stack.append(time)
        
        return len(stack)