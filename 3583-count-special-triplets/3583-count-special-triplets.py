class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        
        m = defaultdict(list)



        for num in range(len(nums)):
            m[nums[num]].append(num)

        print(m)
        ans = 0
        MOD = 10**9 + 7

        for num in range(len(nums)):

            special_num = nums[num] *2

            if special_num not in m or len(m[special_num]) < 2:
                continue

            arr = m[special_num]
            left = bisect.bisect_left(arr, num)
            right = bisect.bisect_right(arr, num)

            total_num_left = left
            total_num_right = len(arr) - right
            ans += (total_num_left*total_num_right) % MOD

        return ans % MOD
        
             

