class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:


        left = [-1 for i in range(len(heights))]
        right = [len(heights)  for i in range(len(heights))]
        maxHeight = 0


        

        s = []
        for i in range(len(heights)):
            while s and heights[s[-1]] > heights[i]:
                curr = s.pop()
                right[curr] = i
            s.append(i)

        """
        3, 2, 6, 5, 1, 2
        """
        s = []
        for i in range(len(heights)-1,-1,-1):
            while s and heights[s[-1]] > heights[i]:
                curr = s.pop()
                left[curr] = i
            s.append(i)

        for i in range(len(left)):
            best = (right[i] - left[i] -1)*heights[i]
            maxHeight = max(maxHeight, best)
        return maxHeight