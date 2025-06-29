class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        a,b,c = False,False,False

        for i in triplets:
            a = a or (i[0] <= target[0] and i[1] <= target[1] and i[2] <= target[2])
            b = b or (i[0] <= target[0] and i[1] == target[1] and i[2] <= target[2])
            c = c or (i[0] <= target[0] and i[1] <= target[1] and i[2] == target[2])

        return a and b and c