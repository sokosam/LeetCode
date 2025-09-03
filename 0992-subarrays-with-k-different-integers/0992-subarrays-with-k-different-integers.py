class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        

        def atMostK(nums, k):
            start = 0
            total = 0
            curr = 0
            m = defaultdict(int)
            for end in range(len(nums)):

                m[nums[end]] += 1

                if m[nums[end]] == 1:
                    curr +=1
                
                while curr > k:
                    m[nums[start]] -= 1
                    if m[nums[start]] == 0:
                        curr -=1
                    start +=1
                
                total += end -start + 1
            return total
        return atMostK(nums, k) - atMostK(nums, k - 1)