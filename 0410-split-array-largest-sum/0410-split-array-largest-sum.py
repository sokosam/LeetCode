class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        l = min(nums)
        r = sum(nums)

        while l <= r:
            m =l + (r-l)//2

            splits = k - 1

            works = True
            curr_sum = 0

            for i in nums:
                if i >m:
                    works = False
                    break
                curr_sum += i
                if curr_sum > m:
                    if splits > 0:
                        curr_sum = i
                        splits -=1
                        continue
                    works = False
                    break
            
            if works:
                r = m -1
            else:
                l = m + 1
        return l





