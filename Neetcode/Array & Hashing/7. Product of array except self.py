class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix product * suffix product
        pref = 1
        suff = 1
        ans = [1]*(len(nums))
        
        for i in range(len(nums)):
            ans[i]*=pref
            pref *= nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=suff
            suff *= nums[i]
        
        return ans
            
        
        
#         result = [0]*len(nums)
#         product = 1
#         countZero = 0
        
#         for num in nums:
#             if num==0:
#                 countZero+=1
#             else:
#                 product*=num
                
#         if countZero==0:
#             for ind,num in enumerate(nums):
#                 result[ind]=product//num
#         elif countZero==1:
#             for ind, num in enumerate(nums):
#                 if num==0:
#                     result[ind] = product
        
#         return result