class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        curr = 1
        ans = 0

        while r < len(nums):
            curr *= nums[r]
            if curr >= k:
                ans += (r-l )*(r-l + 1)//2 
                while curr >= k and l <= r:
                    print(curr, r, l, ans)
                    curr //= nums[l]
                    l += 1
                ans -= (r-l )*(r-l + 1)//2  if (r-l )*(r-l + 1)//2  >= 0 else 0
            r += 1
        ans +=(r-l )*(r-l + 1)//2
        # for i in nums:
        #     if i < k:
        #         ans += 1
        print(ans)
        return max(ans,0)
            
