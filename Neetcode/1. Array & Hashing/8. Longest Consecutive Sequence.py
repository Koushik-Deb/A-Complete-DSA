class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        s = set(nums)
        
        for num in s:
            if num-1 not in s:
                y = num + 1

                while y in s:
                    y+=1

                result = max(result, y-num)
        
        return result