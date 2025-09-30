class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atMost(n):
            nonlocal nums

            m = defaultdict(int)
            unique = 0
            start = 0
            ans = 0
            for end in range(len(nums)):
                m[nums[end]] += 1
                if m[nums[end]] == 1:
                    unique +=1
                
                while unique > n:
                    m[nums[start]] -=1
                    if m[nums[start]] == 0:
                        unique -=1
                    start +=1
                ans += end - start + 1
            return ans
        return atMost(k) - atMost(k -1 )
