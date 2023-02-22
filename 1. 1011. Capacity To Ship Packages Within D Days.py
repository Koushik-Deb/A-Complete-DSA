# Might get done in multiple approach look cautiously
# Follow up question
# What if you were allowed to choose weights in any order, not necessary sequentially as given in the main question? How would you solve this problem.

# Hints

# Still it remains binary search the answer.
# Check of the validity of answer must be done by knapsack DP and not greedy.
# The constraints of the problem must be lower.

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def feasible(weights, cap, days):
            daysNeeded = 1
            currentLoad = 0
            
            for weight in weights:
                currentLoad+=weight
                if (currentLoad>cap):
                    daysNeeded += 1
                    currentLoad = weight
                        
            return daysNeeded<=days
        
        left, right = max(weights), sum(weights)
        while(left<right):
            mid = (left+right)//2
            
            if feasible(weights, mid, days):
                right = mid
            else:
                left = mid+1
            
        return left
            
        
        
        