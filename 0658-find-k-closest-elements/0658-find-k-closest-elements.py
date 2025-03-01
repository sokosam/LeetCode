class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        start = 0

        best = 0

        closeness = 0
        l = 0
        r = k
        for i in range(k):
            closeness += abs(arr[i] - x)
        
        best = closeness
        while r < len(arr):
            removed = abs(arr[l] - x)
            added = abs(arr[r]- x)
            closeness = closeness + added - removed
            if closeness < best:
                best = closeness
                start = l + 1
            
            r += 1
            l+=1
        return arr[start: start + k]



