class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        largest = max(nums)
        smallest = min(nums)
        # prefixRange = [0]*(largest +2)
        m = defaultdict(int)
        prefixLeft = defaultdict(int)
        prefixRight = defaultdict(int)






        for i in range(len(nums)):
            m[nums[i]] += 1
            left = max(smallest, nums[i] - k)
            right = min(nums[i] + k  + 1 ,largest + 1 )
            # prefixRange[left] +=1
            # prefixRange[right] -=1
            prefixLeft[left] +=1
            prefixRight[right] +=1
        
        lowestNum = [[i, m[i]] for i in m]
        leftRange = [[i, prefixLeft[i]] for i in prefixLeft]
        rightRange = [[i, prefixRight[i]] for i in prefixRight]

        heapify(leftRange)
        heapify(rightRange)
        heapify(lowestNum)
        curr = 0
        ans = 0

        left2 = leftRange.copy()
        right2 = rightRange.copy()
        

        add = 0

        while lowestNum:
            curr = heappop(lowestNum)
            while leftRange and leftRange[0][0] <= curr[0]:
                add += heappop(leftRange)[1]
            
            while rightRange and rightRange[0][0] <= curr[0]:
                add -= heappop(rightRange)[1]
            print(add)
            print(leftRange)
            print(rightRange)

            print(lowestNum)
            ans = max(ans, min( add, curr[1] + numOperations))
        print(ans)


        total = 0
        # print(left2,right2)
        while left2:
            while left2:
                if right2 and left2[0][0] >= right2[0][0]:
                    break
                total += heappop(left2)[1]
            # print(total, left2, right2)
            ans = max(ans, min(numOperations,total))
            if right2:
                total -= heappop(right2)[1]
    

        # print(prefixRange)
        # for i in range(len(prefixRange)):
        #     curr += prefixRange[i]
        #     allowed = m[i] + numOperations
        #     ans = max(ans, min(allowed,curr))
        return ans