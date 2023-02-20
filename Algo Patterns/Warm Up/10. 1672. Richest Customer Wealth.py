class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxSum = 0
        
        for account in accounts:
            maxSum = max(maxSum, sum(account))
            
        return maxSum