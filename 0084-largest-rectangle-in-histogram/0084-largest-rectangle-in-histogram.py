class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        smallest = [-1]*len(heights)
        largest = [-1]*len(heights)

        s =[]
        for i in range(len(heights)):
            if len(s) == 0:
                s.append(i)
            else:
                while s and heights[s[-1]] >= heights[i]:
                    s.pop()
            if not s:
                smallest[i] = i
            else:
                smallest[i] = s[-1]
            s.append(i)

        s = []
        for i in range(len(heights)-1,-1,-1):
            if len(s) == 0:
                s.append(i)
            else:
                while s and heights[s[-1]] >= heights[i]:
                    s.pop()
            if not s:
                largest[i] = i
            else:
                largest[i] = s[-1]
            s.append(i)

        # print(smallest, largest)
        ans = 0
        for i in range(len(heights)):
            left,right = 0,0
            if smallest[i] == i:
                left = i 
            else:
                left = i - smallest[i] -1
            if largest[i] == i:
                right = len(heights) - i - 1
            else:
                right = largest[i] - i - 1
            
            ans = max(ans, (left + right + 1)*heights[i] )
        return ans


