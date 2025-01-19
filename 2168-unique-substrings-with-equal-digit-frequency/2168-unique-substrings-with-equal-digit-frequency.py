class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        seen = set()

        for i in range(len(s)):
            l = 0
            r = i
            nums = {}
            for j in range(r):
                if int(s[j]) in nums:
                    nums[int(s[j])] += 1
                else:
                    nums[int(s[j])] = 1      
            # print(nums)

            while r < len(s):
                if int(s[r]) in nums:
                    nums[int(s[r])] += 1
                else:
                    nums[int(s[r])] = 1
                
                dig = -1
                accepted = True
                for val in nums:
                    if dig == -1 and nums[val] != 0:
                        dig = nums[val]
                    else:
                        if dig != nums[val] and nums[val] != 0:
                            accepted = False
                if accepted:
                    seen.add(s[l:r+1])
                nums[int(s[l])] -=1
                r+=1
                l +=1
        return len(seen)