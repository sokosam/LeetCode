class Solution:
    def canSeePersonsCount(self, heights: list[int]) -> list[int]:
        stack = [] 
        ans = [0]*len(heights)

        for i in range(len(heights)-1,-1,-1):
            count = 0
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()
                count += 1
            if not stack:
                ans[i] = count
            else:
                ans[i] = count + 1
            stack.append(i)
        return ans
