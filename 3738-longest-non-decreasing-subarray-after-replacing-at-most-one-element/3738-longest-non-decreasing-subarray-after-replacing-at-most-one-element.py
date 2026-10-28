class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        par = [i for i in range(len(nums))]

        def find(a):
            while par[a] != par[par[a]]:
                par[a] = par[par[a]]         
            return par[a]      

        def union(a,b):
            par[a] = min(find(par[a]), find(par[b]))
            par[b] = min(find(par[a]),find(par[b]))
        
        for idx in range(1, len(nums)):
            if nums[idx] >= nums[idx - 1]:
                union(idx, idx - 1)
        
        c = Counter(par)
        best = max(c.values())
        print(par)

        # for idx in range(1,len(par)):
        #     if par[idx] != par[idx - 1]:
        #         if idx + 1 < len(par) and nums[idx - 1] <= nums[idx + 1]:
        #             best= max(best, c[par[idx]] + c[par[idx- 1]] )
        #         else:
        #             best= max(best, c[par[idx - 1]] + 1)

        if len(par) == 1:
            return 1

        # for idx in range(0,len(par) - 1):
        #     if par[idx] != par[idx + 1]:
        #         if idx + 2 < len(nums):
        #             # 1 par[idx + 1] == par[idx + 2]
        #             if par[idx + 1] == par[idx + 2] and nums[idx] <= nums[idx + 2]:
        #                 best = max(best, c[par[idx]] + c[par[idx + 1]])
        #             # 2, par[idx + 1] != par[idx + 2]
        #             elif par[idx + 1] != par[idx + 2] and nums[idx] <= nums[idx + 2]:
        #                 best = max(best, c[par[idx]] +  c[par[idx + 1]] +  c[par[idx + 2]] )
        #         best = max(c[par[idx]] + 1 , best, 1 + c[par[idx + 1]]) 

        for idx in range(0,len(par) - 1):
            if par[idx] != par[idx + 1]:

                if idx > 0:
                    if nums[idx + 1] >= nums[idx - 1] and par[idx - 1] == par[idx]:
                        best = max(best, c[par[idx + 1]] + c[par[idx]])
                    elif nums[idx + 1] >= nums[idx - 1] and par[idx - 1] != par[idx]:
                        best = max(best, c[par[idx + 1]] + c[par[idx - 1]] + 1)
                if idx + 2 < len(nums):
                    # 1 par[idx + 1] == par[idx + 2]
                    if par[idx + 1] == par[idx + 2] and nums[idx] <= nums[idx + 2]:
                        best = max(best, c[par[idx]] + c[par[idx + 1]])
                    # 2, par[idx + 1] != par[idx + 2]
                    elif par[idx + 1] != par[idx + 2] and nums[idx] <= nums[idx + 2]:
                        best = max(best, c[par[idx]] +  c[par[idx + 1]] +  c[par[idx + 2]] )
                best = max(c[par[idx]] + 1 , best, 1 + c[par[idx + 1]]) 
    




        return best