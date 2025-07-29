class Solution:
    def trap(self, height: List[int]) -> int:
        

        def helper(heights):
            currNeg = 0
            currPos = 0
            ans = 0

            best = 0

            for index,i in enumerate(heights):
                if i ==0 and height[best] ==0:
                    continue
                if i >= height[best]:
                    ans += currPos - currNeg
                    currPos = 0
                    currNeg = 0
                    best = index
                elif i < height[best]:
                    currPos += height[best] 
                    currNeg += i

            return ans, best
        x,y =helper(height)
        
        height = height[y:]
        height.reverse()
        z = helper(height)

        return x + z[0]