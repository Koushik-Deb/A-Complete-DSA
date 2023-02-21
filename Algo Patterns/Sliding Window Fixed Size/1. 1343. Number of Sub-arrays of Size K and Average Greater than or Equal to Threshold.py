class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if k >len(arr): return 0
        result = 0
        total = 0
        for i in range(len(arr)):
            total+=arr[i]
            
            if i>=k:
                total-= arr[i-k]
            
            if i>=k-1 and total//k>=threshold:
                result+=1
        
        return result