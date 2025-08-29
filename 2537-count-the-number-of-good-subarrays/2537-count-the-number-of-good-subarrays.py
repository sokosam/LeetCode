class Solution:
    def countGood(self, nums: List[int], k: int) -> int:



        m = {}

        start = 0
        pairs = 0
        ans = 0


        for end in range(len(nums)):
            number = nums[end]

            if number in m:
                m[number] +=1
            else:
                m[number] = 1
            
            pairs += m[number] - 1

            if pairs >= k:
                ans += len(nums) - end

            while start <= end and pairs >= k:
                number = nums[start]
                m[number] -= 1
                pairs -= m[number]
                if pairs >= k:
                    ans += len(nums) - end
                start +=1
        return ans