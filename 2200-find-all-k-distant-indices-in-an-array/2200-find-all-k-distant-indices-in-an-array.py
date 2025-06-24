class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        


        return(list(set([i for j in range(len(nums)) if nums[j] == key for i in range(max(0, j - k), min(len(nums), j + k + 1))])))

        