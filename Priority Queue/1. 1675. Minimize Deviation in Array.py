class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        pq = []
        ma = 0
        for num in nums:
            newVal = num//(num&-num)
            ma = max(ma, newVal)
            heapq.heappush(pq, [newVal, num])
            
        res = float('inf')
        
        while(len(nums)==len(pq)):
            val, orgVal = heapq.heappop(pq)
            res = min(res, ma-val)
            if val%2 or val<orgVal:
                ma = max(ma, val*2)
                heapq.heappush(pq, [val*2, orgVal])
        return res