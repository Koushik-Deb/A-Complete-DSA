class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = -1
        result = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                left = right
            result = max(result, right-left)
        
        return result