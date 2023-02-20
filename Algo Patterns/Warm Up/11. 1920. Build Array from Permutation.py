class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        newNums = [0]*len(nums)
        
        for ind,num in enumerate(nums):
            newNums[ind] = nums[num]
        
        return newNums
        