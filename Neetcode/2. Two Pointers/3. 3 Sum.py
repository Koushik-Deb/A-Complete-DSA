class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
                
            j = i+1
            k = len(nums)-1
            
            while(j<k):
                val = nums[i]+nums[j]+nums[k]
                
                if val==0:
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while(nums[j]==nums[j-1] and j<k):
                        j+=1
                    
                elif val>0:
                    k-=1
                else:
                    j+=1
        return result