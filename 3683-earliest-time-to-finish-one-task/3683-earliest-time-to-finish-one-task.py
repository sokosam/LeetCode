class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        
        return min([i[0] + i[1] for i in tasks])