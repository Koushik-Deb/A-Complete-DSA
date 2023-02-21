class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        dt = defaultdict(int)
        result = 0
        k = 3
        for i in range(len(s)):
            dt[s[i]] += 1
            
            if i>=k:
                dt[s[i-k]] -= 1
                if dt[s[i-k]]<=0:
                    del dt[s[i-k]]            
            if i>=k-1 and len(dt)==k:
                result+=1
        return result
                