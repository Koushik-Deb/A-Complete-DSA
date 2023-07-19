from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dt = defaultdict(list)
        
        for word in strs:
            ls = list(word)
            ls.sort()
            dt[tuple(ls)].append(word)
    
        for key in dt.keys():
            result.append(dt[key])
        
        return result