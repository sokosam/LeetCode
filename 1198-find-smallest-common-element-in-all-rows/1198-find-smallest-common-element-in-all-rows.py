class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        counts = defaultdict(int)

        for row in mat:
            for col in row:
                counts[col] +=1
        
        x = [i for i in counts if counts[i] == len(mat)]
        if len(x) == 0:
            return -1
        else: return min(x)