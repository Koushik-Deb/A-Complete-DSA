class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        result = 0
        dt = defaultdict(int)

        for right in range(len(s)):
            dt[s[right]]+=1
            
            while(left<right and dt[s[right]]>1):
                dt[s[left]]-=1
                if dt[s[left]]<=0: del dt[s[left]]

                left+=1

            result = max(result, right-left+1)
        return result