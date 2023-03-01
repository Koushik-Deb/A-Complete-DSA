class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = -999999
        curSum = 0
        for i in range(len(nums)):
            curSum+=nums[i]
            if i>=k-1:
                maxSum = max(maxSum, curSum/k)
                curSum -= nums[i-k+1]
        return maxSum