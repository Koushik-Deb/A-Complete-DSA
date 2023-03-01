class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        result = []

        if len(p)>len(s): return result
        dtP = defaultdict(int)
        dtS = defaultdict(int)

        def isValid(fs,sd): return fs==sd

        for c in p:
            dtP[c]+=1
        
        for i in range(len(s)):
            dtS[s[i]] += 1
            
            if i>=len(p):
                dtS[s[i-len(p)]]-=1
                if dtS[s[i-len(p)]]<=0:
                    del dtS[s[i-len(p)]]
                    
            if isValid(dtS,dtP):    result.append(i+1-len(p))


        return result
