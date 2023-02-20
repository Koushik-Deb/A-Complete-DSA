class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dt = defaultdict(int)
        
        for num in nums:
            dt[num]+=1
        
        result = 0
        
        for key in dt.keys():
            val = dt[key]
            if val>1:
                result+= (val*(val-1))//2
        return result
        