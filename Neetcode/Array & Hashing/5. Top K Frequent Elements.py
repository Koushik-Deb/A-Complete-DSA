from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = list(count.keys())
        
        def partition(low, high):
            pivot = arr[high]
            i = low
            for j in range(low, high):
                if count[arr[j]]<count[pivot]:
                    arr[i],arr[j] = arr[j],arr[i]
                    i+=1
            arr[i],arr[high] = arr[high],arr[i]
            return i
        
        def quickSelect(low, high, k):
            if low<high:
                pivot = partition(low, high)
                
                if pivot==k:
                    return
                elif pivot<k:
                    quickSelect(pivot+1, high,k)
                else:
                    quickSelect(low,pivot-1,k)
                    
        quickSelect(0, len(arr)-1,len(arr)-k)
        return arr[len(arr)-k:]