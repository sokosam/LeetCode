class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
            return all([any([True for i in triplets if i[0] == target[0] and i[1] <= target[1] and i[2] <= target[2]]),any([True for i in triplets if i[0] <= target[0] and i[1] == target[1] and i[2] <= target[2]]),any([True for i in triplets if i[0] <= target[0] and i[1] <= target[1] and i[2] == target[2]])])